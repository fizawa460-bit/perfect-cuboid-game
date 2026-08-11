#!/usr/bin/env python3

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def factor(n: int):
    out = []
    p = 2
    while p * p <= n:
        if n % p == 0:
            e = 0
            while n % p == 0:
                n //= p
                e += 1
            out.append((p, e))
        p += 1 if p == 2 else 2
    if n > 1:
        out.append((n, 1))
    return out


def phi(n: int) -> int:
    ans = n
    for p, _ in factor(n):
        ans = ans // p * (p - 1)
    return ans


def split_squarefree(n: int) -> bool:
    fs = factor(n)
    return n > 1 and all(e == 1 and p % 4 == 1 for p, e in fs)


def roots_minus_one(n: int):
    return [r for r in range(n) if (r * r + 1) % n == 0]


def primitive_box_density(c: int, m: int):
    total = 0
    hit = 0
    for x in range(1, m + 1):
        for y in range(1, m + 1):
            if math.gcd(x, y) != 1:
                continue
            if math.gcd(c, x * y) != 1:
                continue
            total += 1
            if (x * x + y * y) % c == 0:
                hit += 1
    return hit, total


def require(path: str, needles):
    text = (ROOT / path).read_text()
    for needle in needles:
        assert needle in text, (path, needle)
    return text


def main():
    require(
        "stages/stage14/H-PROTOCOL.md",
        [
            "ONE_H_REQUEST_ONE_SNAPSHOT=true",
            "RUNNING_H_CHASES_LATER_PARENT_STAGES=false",
            "COMPLETED_H_MERGES_AS_SCOPED_SNAPSHOT_RESULT=true",
        ],
    )

    require(
        "stages/stage14/14-s7-71/result.md",
        [
            "STAGE14_S7_71=COMPLETE_PRIMITIVE_GAUSSIAN_ROOT_DENSITY_BOUNDARY_AND_SH71_GATE",
            "SECOND_RECIPROCAL_ROOT_LINE_MODULUS_IS_C0=true",
            "INDEPENDENT_SECOND_GROWING_MODULUS_PRODUCED=false",
            "FRESH_DIVISOR_SWITCH_POWER_SAVING_PROVED=false",
            "PRIMITIVE_GAUSSIAN_ROOT_CONDITIONAL_DENSITY_THEOREM_PROVED=false",
            "S7_71_AUXILIARY_H_TARGET=CanonicalAllocationConditionalPrimitiveGaussianRootDensity",
            "S_ROUTE_BLOCKED_WAITING_FOR_H=true",
            "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
            "STRICT_SUBSQRT_POWER_SAVING_PROVED=false",
            "NEXT=Stage14-sH71",
        ],
    )

    require(
        "stages/stage14/14-s7-71/sh71-target.md",
        [
            "H_STAGE=Stage14-sH71",
            "SOURCE_SNAPSHOT_SHA=76bc8a4e59d8d220c58552e42dafef7d12ef55a3",
            "REQUESTED_OBJECT=CanonicalAllocationConditionalPrimitiveGaussianRootDensity",
            "TARGET_FROZEN=true",
            "C0 | X0^2+Y0^2",
            "CANONICAL_BACKGROUND_PSEUDORANDOMNESS_ADAPTER_PROVED=true|false",
        ],
    )

    require(
        "stages/stage14/14-sH71/BOUNDARY.txt",
        [
            "STAGE14_SH71=COMPLETE_S7_71_SNAPSHOT_CANONICAL_ALLOCATION_CONDITIONAL_PRIMITIVE_GAUSSIAN_ROOT_DENSITY_APPLICABILITY_AUDIT",
            "C0_FIXED_POWER_LOWER_BOUND_PROVED=false",
            "ROOT_LINE_PRINCIPAL_DENSITY_UNIFORMLY_POWER_SPARSE=false",
            "DIRECT_GAUSSIAN_ROOT_EQUIDISTRIBUTION_THEOREM_APPLICABLE=false",
            "ROOT_LARGE_SIEVE_DIRECTLY_APPLICABLE=false",
            "BILINEAR_ROOT_DISPERSION_DIRECTLY_APPLICABLE=false",
            "DIVISOR_CORRELATED_NORM_FORM_SIEVE_DIRECTLY_APPLICABLE=false",
            "CANONICAL_BACKGROUND_PSEUDORANDOMNESS_ADAPTER_PROVED=false",
            "UNIFORM_FIXED_POWER_CONDITIONAL_DENSITY_SAVING_PROVED=false",
            "CERTIFIED_CONDITIONAL_DENSITY_SAVING_EXPONENT=0",
            "NEXT_H_NEEDED=false",
            "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2",
        ],
    )

    data = json.loads(
        (ROOT / "stages/stage14/data/sH71/canonical_allocation_gaussian_root_density_boundary.json").read_text()
    )
    assert data["stage"] == "14-sH71"
    assert data["target_frozen"] is True
    b = data["boundary"]
    assert b["UNIFORM_FIXED_POWER_CONDITIONAL_DENSITY_SAVING_PROVED"] is False
    assert b["CERTIFIED_CONDITIONAL_DENSITY_SAVING_EXPONENT"] == "0"
    assert b["NEXT_H_NEEDED"] is False

    modulus_checks = 0
    root_checks = 0
    density_formula_checks = 0
    max_roots = 0
    for c in range(3, 301, 2):
        if not split_squarefree(c):
            continue
        roots = roots_minus_one(c)
        expected = 2 ** len(factor(c))
        assert len(roots) == expected, (c, roots, expected)
        assert all(math.gcd(r, c) == 1 for r in roots)
        max_roots = max(max_roots, len(roots))
        modulus_checks += 1
        root_checks += len(roots)
        unit_pair_hits = 0
        unit_pairs = 0
        for x in range(c):
            if math.gcd(x, c) != 1:
                continue
            for y in range(c):
                if math.gcd(y, c) != 1:
                    continue
                unit_pairs += 1
                if (x * x + y * y) % c == 0:
                    unit_pair_hits += 1
        assert unit_pairs == phi(c) ** 2
        assert unit_pair_hits == len(roots) * phi(c)
        density_formula_checks += 1

    box_guards = {}
    for c in (5, 13, 65):
        hit, total = primitive_box_density(c, 160)
        assert hit > 0 and total > 0
        ratio = hit / total
        assert ratio > 0.01
        box_guards[str(c)] = {"hits": hit, "total": total, "density": ratio}

    assert len(roots_minus_one(5)) / phi(5) == 0.5
    assert len(roots_minus_one(13)) / phi(13) == 1 / 6

    out = {
        "stage": "14-sH71",
        "status": "COMPLETE_S7_71_SNAPSHOT_CANONICAL_ALLOCATION_CONDITIONAL_PRIMITIVE_GAUSSIAN_ROOT_DENSITY_APPLICABILITY_AUDIT",
        "split_squarefree_modulus_checks": modulus_checks,
        "root_orientation_checks": root_checks,
        "unit_pair_density_formula_checks": density_formula_checks,
        "max_roots_in_sample": max_roots,
        "fixed_modulus_primitive_box_guards": box_guards,
        "principal_density_C5": "1/2",
        "principal_density_C13": "1/6",
        "boundary": b,
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
