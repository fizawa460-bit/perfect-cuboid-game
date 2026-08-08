#!/usr/bin/env python3
"""Stage13-12aa: non-circular j=0 common-factor audit.

This script audits the algebraic inputs for the Stage13-12aa repair of the
raw-incidence directional theorem. It deliberately does NOT seed categorywise
raw constants from the Stage12 total theorem.

The theorem proof is in stages/stage13/13-12aa/result.md. This script checks:
  * the exact j=0 primitive local kernels;
  * the closed pure h/base generating factors;
  * cancellation of all pure-axis terms in the mixed correction;
  * a sampled weighted-l1 norm consistent with O(q^(-1-2 delta));
  * the chamber bridge J_q=(2/pi)I_q and sum J_q=pi/4;
  * the final calibration algebra after the common-factor lemma is established.
"""
from __future__ import annotations

import json
import math
from collections import defaultdict
from pathlib import Path

ROOT = Path("stages/stage13")
IN_CHAMBER = ROOT / "data/13-3/geometric_chamber_report.json"
OUT = ROOT / "data/13-12aa/j0_common_factor_audit_report.json"
CATS = ("ab", "ac", "bc")
SPLIT_PRIMES = (5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97)
ELLS = (1, 2, 5, 17)


def dirichlet_kernel(e: int, phase: float) -> float:
    return 1.0 + 2.0 * sum(math.cos(m * phase) for m in range(1, e + 1))


def local_j0(mode: str, phase: float, a: int, b: int) -> float:
    """Exact split-prime primitive raw coefficient.

    a=v_q(h), b=v_q(rs), e=a+b. Since gcd(r,s)=1 the exponent b belongs to
    at most one base variable.
    """
    e = a + b
    if mode == "zero":
        return float(2 * b + 1) if a == 0 else 2.0
    if a == 0:
        return dirichlet_kernel(b, phase)
    return 2.0 * math.cos(e * phase)


def pure_h_closed(x: complex, phase: float) -> complex:
    c = math.cos(phase)
    return (1.0 - x * x) / (1.0 - 2.0 * c * x + x * x)


def pure_base_closed(x: complex, phase: float) -> complex:
    c = math.cos(phase)
    return (1.0 + x) / (1.0 - 2.0 * c * x + x * x)


def inv_1d(coeff: list[float]) -> list[float]:
    out = [0.0] * len(coeff)
    out[0] = 1.0
    for n in range(1, len(coeff)):
        out[n] = -sum(coeff[k] * out[n - k] for k in range(1, n + 1))
    return out


def conv3(
    A: dict[tuple[int, int, int], float],
    B: dict[tuple[int, int, int], float],
    N: int,
) -> dict[tuple[int, int, int], float]:
    out: dict[tuple[int, int, int], float] = defaultdict(float)
    for i, x in A.items():
        for j, y in B.items():
            idx = tuple(i[k] + j[k] for k in range(3))
            if max(idx) <= N:
                out[idx] += x * y
    return dict(out)


def correction_coefficients(mode: str, phase: float, N: int = 8):
    """Truncated C=D/(A_h B_r B_s) at a split prime."""
    D: dict[tuple[int, int, int], float] = {(0, 0, 0): 1.0}
    for a in range(1, N + 1):
        D[(a, 0, 0)] = local_j0(mode, phase, a, 0)
    for b in range(1, N + 1):
        v = local_j0(mode, phase, 0, b)
        D[(0, b, 0)] = v
        D[(0, 0, b)] = v
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            v = local_j0(mode, phase, a, b)
            D[(a, b, 0)] = v
            D[(a, 0, b)] = v

    Avec = [1.0] + [local_j0(mode, phase, a, 0) for a in range(1, N + 1)]
    Bvec = [1.0] + [local_j0(mode, phase, 0, b) for b in range(1, N + 1)]
    iA, iB = inv_1d(Avec), inv_1d(Bvec)
    IA = {(a, 0, 0): iA[a] for a in range(N + 1)}
    IR = {(0, b, 0): iB[b] for b in range(N + 1)}
    IS = {(0, 0, c): iB[c] for c in range(N + 1)}
    return conv3(conv3(conv3(D, IA, N), IR, N), IS, N)


def split_prime_angle(q: int) -> float:
    for a in range(1, math.isqrt(q) + 1):
        b2 = q - a * a
        if b2 <= 0:
            continue
        b = math.isqrt(b2)
        if b * b == b2:
            x, y = sorted((a, b))
            return math.atan2(x, y)
    raise ValueError(q)


def coefficient_identity_audit() -> dict:
    phase = 0.731234567
    max_zero = 0.0
    max_harm = 0.0
    cases = 0
    for a in range(7):
        for b in range(7):
            e = a + b
            G_e = 2 * e + 1
            G_prev = 2 * (e - 1) + 1 if e else 0
            zero_direct = float(G_e if a == 0 else G_e - G_prev)
            H_e = dirichlet_kernel(e, phase)
            H_prev = dirichlet_kernel(e - 1, phase) if e else 0.0
            harm_direct = H_e if a == 0 else H_e - H_prev
            max_zero = max(max_zero, abs(zero_direct - local_j0("zero", phase, a, b)))
            max_harm = max(max_harm, abs(harm_direct - local_j0("harmonic", phase, a, b)))
            cases += 1
    return {
        "cases": cases,
        "max_zero_error": max_zero,
        "max_harmonic_error": max_harm,
    }


def closed_form_audit() -> dict:
    phase = 0.731234567
    radii = (0.03, 0.1, 0.2)
    max_h = max_b = 0.0
    for x in radii:
        h_partial = 1.0 + sum(
            local_j0("harmonic", phase, a, 0) * x**a for a in range(1, 80)
        )
        b_partial = 1.0 + sum(
            local_j0("harmonic", phase, 0, b) * x**b for b in range(1, 80)
        )
        max_h = max(max_h, abs(h_partial - pure_h_closed(x, phase)))
        max_b = max(max_b, abs(b_partial - pure_base_closed(x, phase)))
    return {
        "max_pure_h_closed_form_error": max_h,
        "max_pure_base_closed_form_error": max_b,
        "zero_mode_pure_h": "(1+x)/(1-x)",
        "zero_mode_pure_base": "(1+x)/(1-x)^2",
        "harmonic_pure_h": "(1-x^2)/(1-2*cos(theta)*x+x^2)",
        "harmonic_pure_base": "(1+x)/(1-2*cos(theta)*x+x^2)",
    }


def correction_audit() -> dict:
    delta = 0.05
    sigma = 0.5 + delta
    max_pure_axis_error = 0.0
    max_scaled_norm = 0.0
    rows = []

    specs = [("zero", 0, q, 0.0) for q in SPLIT_PRIMES]
    specs += [
        ("harmonic", ell, q, 8.0 * ell * split_prime_angle(q))
        for ell in ELLS
        for q in SPLIT_PRIMES
    ]

    for mode, ell, q, phase in specs:
        C = correction_coefficients(mode, phase, N=8)
        pure = max(
            (
                abs(value)
                for idx, value in C.items()
                if idx != (0, 0, 0) and sum(v > 0 for v in idx) <= 1
            ),
            default=0.0,
        )
        norm = sum(
            abs(value) * q ** (-sigma * sum(idx))
            for idx, value in C.items()
            if idx != (0, 0, 0)
        )
        scaled = norm * q ** (1.0 + 2.0 * delta)
        max_pure_axis_error = max(max_pure_axis_error, pure)
        max_scaled_norm = max(max_scaled_norm, scaled)
        if q in (5, 97):
            rows.append(
                {
                    "mode": mode,
                    "ell": ell,
                    "q": q,
                    "pure_axis_error": pure,
                    "truncated_weighted_norm": norm,
                    "q^(1+2delta)_scaled_norm": scaled,
                }
            )

    return {
        "delta": delta,
        "truncation_exponent_cap": 8,
        "max_pure_axis_error": max_pure_axis_error,
        "max_sampled_q^(1+2delta)_scaled_norm": max_scaled_norm,
        "sample_rows": rows,
        "theorem_interpretation": (
            "Pure-axis cancellation is exact. The proof uses uniform Wiener-algebra "
            "bounds on the rational pure factors to obtain ||C_q-1||_delta="
            "O_delta(q^(-1-2delta)); the finite rows are diagnostics only."
        ),
    }


def build_report() -> dict:
    chamber = json.loads(IN_CHAMBER.read_text())
    I = {
        q: float(chamber["numerical_chamber_integrals"][f"I_{q}"])
        for q in CATS
    }
    J = {q: 2.0 * I[q] / math.pi for q in CATS}
    if abs(sum(J.values()) - math.pi / 4.0) > 2e-12:
        raise ArithmeticError("J_q chamber partition failed")

    prop = {q: J[q] / sum(J.values()) for q in CATS}
    ratio = {
        "ab": J["ab"] / J["bc"],
        "ac": J["ac"] / J["bc"],
        "bc": 1.0,
    }

    return {
        "metadata": {
            "stage": "13-12aa",
            "scope": "non-circular j=0 common-factor repair audit",
        },
        "review_reopening": {
            "old_7jb_categorywise_constant_check_is_independent_proof": False,
            "reason": (
                "The old validator first formed D_q from the Stage12 total times the "
                "chamber proportion and then checked D_q/K_q; because K_q is already "
                "proportional to I_q, equality of the three ratios is algebraic."
            ),
            "old_7jb_kept_as": "provenance/diagnostic only",
        },
        "exact_j0_local_kernel": {
            "zero": "a=0: 2b+1; a>=1: 2",
            "harmonic": "a=0: D_b(theta); a>=1: 2 cos((a+b)theta)",
            "primitive_origin": (
                "G_{a+b} - 1_{a>=1}G_{a+b-1} and "
                "H_{a+b} - 1_{a>=1}H_{a+b-1}"
            ),
            "audit": coefficient_identity_audit(),
        },
        "pure_factor_closed_forms": closed_form_audit(),
        "mixed_correction": correction_audit(),
        "dirichlet_singularity": {
            "zero_scale": "A_0(s)=zeta(s)L(s,chi4)E_h,0(s)",
            "zero_base": "B_0(s)=zeta(s)^2 L(s,chi4)E_b,0(s)",
            "harmonic_scale": "A_l(s)=L(s,xi_8l)E_h,l(s), l>=1",
            "harmonic_base": "B_l(s)=zeta(s)L(s,xi_8l)E_b,l(s), l>=1",
            "mixed_factor": (
                "C_l(s_h,s_r,s_s) is absolutely convergent in the same "
                "weighted-l1 half-plane Re(s_i)>=1/2+delta."
            ),
        },
        "common_factor_theorem_shape": {
            "statement": "A_q(B) ~ Theta * J_q * B(log B)^3 with one Theta for all q",
            "category_dependence_only": "J_q=int k_q(t(phi)) dphi",
            "J": J,
            "sum_J": sum(J.values()),
            "expected_sum_J": math.pi / 4.0,
        },
        "harmonic_remainder": {
            "method": (
                "Pointwise Selberg/Vaaler bracketing with L=(log B)^K, plus "
                "polylog-uniform nontrivial Gaussian-Hecke cancellation in the h-factor."
            ),
            "zero_coefficient_bracketing_error": "O(B(log B)^3/L)",
            "retained_nonzero_harmonics": "o(B(log B)^3)",
            "small_height_boundary": "o(B(log B)^3)",
        },
        "non_circular_stage12_calibration": {
            "input_used_only_after_common_factor": (
                "sum_q A_q(B) ~ [kappa/(24*pi)]B(log B)^3"
            ),
            "Theta": "kappa/(6*pi^2)",
            "J_to_I": "J_q=2 I_q/pi",
            "deduction": "D_q=Theta J_q=kappa I_q/(3*pi^3)",
            "categorywise_D_q_seeded_before_common_factor_proof": False,
        },
        "restored_raw_normalized_limit": {
            "proportion": prop,
            "bc_normalized_ratio": ratio,
        },
        "status": {
            "claude_fatal_direction_neutrality_repaired": True,
            "raw_directional_common_factor_proved_at_project_external_theorem_level": True,
            "raw_directional_constants_calibrated_non_circularly": True,
            "exact_one_stage13_reclosed": False,
            "pending": "13-12ab independent overlap fixed-modulus transfer audit",
        },
    }


def main() -> None:
    report = build_report()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report["status"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
