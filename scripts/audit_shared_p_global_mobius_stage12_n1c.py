#!/usr/bin/env python3
"""Stage12-N1c: reduce primitive shared-p counting to global Mobius inversion."""
from __future__ import annotations

import argparse
import json
import math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from audit_shared_p_convolution_stage11 import MAX_D, THRESHOLDS, build_spf, enumerate_shared_p
from audit_shared_p_primitive_joint_stage12_n1b import divisors, mobius_sieve

DEFAULT_REPORT = Path("data/shared_p_global_mobius_stage12_n1c_report.json")


def prefix(values: list[int]) -> list[int]:
    out = [0] * len(values)
    running = 0
    for i, value in enumerate(values):
        running += value
        out[i] = running
    return out


def build_report() -> dict[str, Any]:
    triangles, _, records, _ = enumerate_shared_p(MAX_D)
    mu = mobius_sieve(MAX_D)
    spf = build_spf(MAX_D)

    raw_all_exact = [0] * (MAX_D + 1)
    raw_distinct_exact = [0] * (MAX_D + 1)
    repeated_exact = [0] * (MAX_D + 1)
    first_by_p: dict[int, list[tuple[int, int, int]]] = defaultdict(list)

    for x in range(1, MAX_D + 1):
        for y, p, _, _ in triangles[x]:
            if x < y:
                first_by_p[p].append((x, y, math.gcd(x, y)))
            for c, d, _, _ in triangles[p]:
                raw_all_exact[d] += 1
                if len({x, y, c}) == 3:
                    raw_distinct_exact[d] += 1
                else:
                    repeated_exact[d] += 1

    raw_all_prefix = prefix(raw_all_exact)
    raw_distinct_prefix = prefix(raw_distinct_exact)
    repeated_prefix = prefix(repeated_exact)

    primitive_exact = [0] * (MAX_D + 1)
    for (_, _, _, d), record in records.items():
        primitive_exact[d] += int(record["oriented_chain_count"])
    primitive_prefix = prefix(primitive_exact)

    # Check A_k(p)=H(p/k): divisibility of the first-triangle scale.
    a_identity_checks = 0
    a_identity_mismatches: list[dict[str, int]] = []
    h_counts = {p: len(reps) for p, reps in first_by_p.items()}
    for p, reps in first_by_p.items():
        for k in divisors(p, spf):
            actual = sum(1 for _, _, g in reps if g % k == 0)
            expected = h_counts.get(p // k, 0)
            a_identity_checks += 1
            if actual != expected:
                a_identity_mismatches.append({"p": p, "k": k, "actual": actual, "expected": expected})
                if len(a_identity_mismatches) >= 5:
                    break
        if a_identity_mismatches:
            break
    if a_identity_mismatches:
        raise ArithmeticError(f"A_k scaling identity failed: {a_identity_mismatches}")

    # Check B_{k,B}(p)=L_{floor(B/k)}(p/k) whenever k|p.
    b_identity_checks = 0
    b_identity_mismatches: list[dict[str, int]] = []
    for B in THRESHOLDS:
        for p in range(1, B + 1):
            for k in divisors(p, spf):
                actual = sum(1 for c, d, _, _ in triangles[p] if d <= B and c % k == 0)
                q = p // k
                expected = sum(1 for _, d, _, _ in triangles[q] if d <= B // k)
                b_identity_checks += 1
                if actual != expected:
                    b_identity_mismatches.append(
                        {"B": B, "p": p, "k": k, "actual": actual, "expected": expected}
                    )
                    if len(b_identity_mismatches) >= 5:
                        break
            if b_identity_mismatches:
                break
        if b_identity_mismatches:
            break
    if b_identity_mismatches:
        raise ArithmeticError(f"B_k scaling identity failed: {b_identity_mismatches}")

    rows = []
    for B in THRESHOLDS:
        mobius_distinct = sum(mu[k] * raw_distinct_prefix[B // k] for k in range(1, B + 1))
        if mobius_distinct != primitive_prefix[B]:
            raise ArithmeticError(
                f"global Mobius inversion failed at B={B}: {mobius_distinct} != {primitive_prefix[B]}"
            )
        rows.append(
            {
                "B": B,
                "raw_all_oriented": raw_all_prefix[B],
                "raw_distinct_oriented": raw_distinct_prefix[B],
                "raw_repeated_side_oriented": repeated_prefix[B],
                "global_mobius_of_distinct_raw": mobius_distinct,
                "stage11_primitive_oriented": primitive_prefix[B],
            }
        )

    return {
        "metadata": {
            "stage": "12-N1c",
            "title": "Global Mobius inversion of the distinct shared-p convolution",
            "generated_by": "scripts/audit_shared_p_global_mobius_stage12_n1c.py",
            "claim_status": "All identities and finite checks are exact. No asymptotic estimate is claimed.",
        },
        "exact_identites": {
            "A_scaling": "A_k(p)=H(p/k) if k|p, and 0 otherwise",
            "B_scaling": "B_{k,B}(p)=L_{floor(B/k)}(p/k) if k|p",
            "joint_reduction": "J_B(p)=sum_{k|p}mu(k)H(p/k)L_{floor(B/k)}(p/k)",
            "global_inversion": "C_prim(B)=sum_{k<=B}mu(k)C_distinct_raw(floor(B/k))",
            "forward_scaling": "C_distinct_raw(B)=sum_{k<=B}C_prim(floor(B/k))",
        },
        "checks": {
            "A_identity_cases": a_identity_checks,
            "A_identity_mismatches": 0,
            "B_identity_cases": b_identity_checks,
            "B_identity_mismatches": 0,
        },
        "finite_rows": rows,
        "decision": {
            "confirmed": [
                "The primitive-compatible joint weight collapses to scaled copies of H and L.",
                "After separating repeated-side chains, primitive oriented counting is the exact Mobius inversion of the distinct raw convolution.",
                "The primitive correction is therefore algebraically closed, not an unknown local-density factor.",
            ],
            "not_claimed": [
                "That repeated-side chains are absent for all heights.",
                "An asymptotic for the distinct raw convolution or its Mobius inversion.",
                "A lower bound for N1 stronger than Stage11.",
            ],
            "next_question": (
                "Does C_distinct_raw(B) have an asymptotic with enough uniform error control under B->floor(B/k) "
                "to survive Mobius inversion and improve the primitive N1 lower bound?"
            ),
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-report", type=Path, default=DEFAULT_REPORT)
    args = parser.parse_args()
    report = build_report()
    args.write_report.parent.mkdir(parents=True, exist_ok=True)
    args.write_report.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["decision"], ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
