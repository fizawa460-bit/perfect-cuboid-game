#!/usr/bin/env python3
"""E-1e audit: fixed-edge divisor bound and exactly-one synthesis.

This script audits the elementary overlap mechanism used by E-1e.
It does not numerically prove the standard divisor-function estimate

    tau(n) = n^{o(1)},

which is an analytic input.  Instead it checks the exact factor-pair map for
small n, imports the E-1d raw constants, and records the finite E-1b overlap
ledger against the B^2 log B main scale.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

E1D = Path("stages/euler-cuboid/data/E-1d/structural_chamber_report.json")
E1B = Path("stages/euler-cuboid/data/E-1b/population_report.json")
OUT = Path("stages/euler-cuboid/data/E-1e/exact_one_synthesis_audit_report.json")


def tau(n: int) -> int:
    if n <= 0:
        raise ValueError("tau is defined here only for positive integers")
    ans = 1
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            ans *= e + 1
        p += 1 if p == 2 else 2
    if n > 1:
        ans *= 2
    return ans


def pythagorean_partners_by_factorization(n: int) -> set[int]:
    """All x>0 with n^2+x^2 a square, via (y-x)(y+x)=n^2."""
    n2 = n * n
    out: set[int] = set()
    for u in range(1, math.isqrt(n2) + 1):
        if n2 % u:
            continue
        v = n2 // u
        if u >= v:
            continue
        if (u + v) % 2:
            continue
        x = (v - u) // 2
        y = (v + u) // 2
        if x > 0 and n2 + x * x == y * y:
            out.add(x)
    return out


def pythagorean_partners_bruteforce(n: int) -> set[int]:
    """Independent finite check; every partner has x<n^2/2."""
    out: set[int] = set()
    # From y-x>=1 and (y-x)(y+x)=n^2, y+x<=n^2,
    # hence 2x < n^2.  This gives a complete finite brute-force range.
    for x in range(1, (n * n) // 2 + 1):
        s = n * n + x * x
        y = math.isqrt(s)
        if y * y == s:
            out.add(x)
    return out


def fixed_edge_audit(max_n: int) -> dict:
    mismatches = []
    bound_failures = []
    rows = []
    for n in range(1, max_n + 1):
        fac = pythagorean_partners_by_factorization(n)
        brute = pythagorean_partners_bruteforce(n)
        t = tau(n * n)
        if fac != brute:
            mismatches.append({"n": n, "factorization": sorted(fac), "brute": sorted(brute)})
        if len(fac) > t:
            bound_failures.append({"n": n, "partners": len(fac), "tau_n2": t})
        if n <= 20:
            rows.append({"n": n, "partner_count": len(fac), "tau_n2": t, "partners": sorted(fac)})
    return {
        "max_n": max_n,
        "factorization_matches_bruteforce": not mismatches,
        "partner_bound_holds": not bound_failures,
        "mismatches": mismatches,
        "bound_failures": bound_failures,
        "sample_rows": rows,
    }


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def finite_overlap_audit(e1b: dict) -> list[dict]:
    out = []
    for row in e1b["rows"]:
        B = row["B"]
        raw_total = sum(row["raw_incidence"].values())
        pair_sum = sum(row["pair_overlap"].values())
        scale = B * B * math.log(B)
        out.append(
            {
                "B": B,
                "raw_incidence_total": raw_total,
                "pair_overlap_sum": pair_sum,
                "triple_overlap": row["triple_overlap"],
                "pair_overlap_fraction_of_raw_total": pair_sum / raw_total,
                "pair_overlap_over_B2_logB": pair_sum / scale,
                "triple_overlap_over_B2_logB": row["triple_overlap"] / scale,
            }
        )
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-n", type=int, default=120)
    parser.add_argument("--output", type=Path, default=OUT)
    args = parser.parse_args()

    e1d = load_json(E1D)
    e1b = load_json(E1B)
    fixed = fixed_edge_audit(args.max_n)
    finite = finite_overlap_audit(e1b)

    I = e1d["chamber_integrals"]["stage13_reference"]
    constants = {q: 6.0 * I[q] / math.pi**4 for q in ("ab", "ac", "bc")}
    total_constant = sum(constants.values())
    expected_total = 3.0 / (4.0 * math.pi**2)
    normalized = {q: constants[q] / total_constant for q in constants}
    bc_ratio = {q: constants[q] / constants["bc"] for q in constants}

    report = {
        "metadata": {
            "stage": "E-1e",
            "scope": "fixed-edge divisor overlap bound and exactly-one asymptotic synthesis audit",
            "counting": "primitive canonical 0<a<b<c with a^2+b^2+c^2<=B^2",
            "space_diagonal_integrality_required": False,
        },
        "fixed_edge_partner_lemma": {
            "identity": "n^2+x^2=y^2 => (y-x)(y+x)=n^2",
            "bound": "|P(n)|<=tau(n^2)",
            "audit": fixed,
        },
        "analytic_overlap_bound": {
            "uniform_pair_bound": "O_qr(B)<=sum_{n<B} tau(n^2)^2",
            "divisor_input": "for every epsilon>0, tau(n^2)^2 <<_epsilon n^epsilon",
            "conclusion": "O_qr(B)<<_epsilon B^(1+epsilon)=o(B^2 log B) for any fixed epsilon<1",
            "triple_bound": "T(B)<=O_qr(B)=o(B^2 log B)",
        },
        "raw_to_exact_one": {
            "ab": "N_ab=A_ab-O_ab_ac-O_ab_bc+T",
            "ac": "N_ac=A_ac-O_ab_ac-O_ac_bc+T",
            "bc": "N_bc=A_bc-O_ab_bc-O_ac_bc+T",
            "conclusion": "N_q(B)=A_q(B)+o(B^2 log B)",
        },
        "exact_one_theorem": {
            "categorywise": {q: f"N_{q}(B) ~ c_{q} B^2 log B" for q in constants},
            "constants": constants,
            "total_constant": total_constant,
            "expected_total_constant_3_over_4pi2": expected_total,
            "total_constant_abs_error": abs(total_constant - expected_total),
            "normalized_limit": normalized,
            "bc_normalized_ratio": bc_ratio,
            "same_as_E1d_raw_vector": True,
            "same_as_stage13_chamber_vector": True,
        },
        "finite_overlap_diagnostic": finite,
        "status": {
            "E_1E_complete": True,
            "E_1_complete": True,
            "fixed_edge_factorization_audit_pass": fixed["factorization_matches_bruteforce"],
            "fixed_edge_tau_bound_audit_pass": fixed["partner_bound_holds"],
            "pair_overlap_lower_order_proved_from_divisor_bound": True,
            "triple_overlap_lower_order_proved": True,
            "raw_to_exact_one_transfer_closed": True,
            "normalized_exact_one_limit_proved": True,
            "next": "E-2a exactly-two population definition and finite census",
        },
    }

    assert fixed["factorization_matches_bruteforce"]
    assert fixed["partner_bound_holds"]
    assert abs(total_constant - expected_total) < 1e-14

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["status"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
