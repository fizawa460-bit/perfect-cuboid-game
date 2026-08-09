#!/usr/bin/env python3
"""Deterministic architecture audit for Stage14-s6-00.

This stage is a route-selection / exponent-budget stage, not a numerical
experiment.  The audit locks the exact s5u -> s6 exponent arithmetic, checks
that the fixed M-degree-4 mechanism is already closed upstream, and freezes the
selected direct global-small-point route and provisional 00..09 roadmap.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]


def read(path: str) -> str:
    p = ROOT / path
    assert p.exists(), p
    return p.read_text(encoding="utf-8")


def find_archive(token: str) -> tuple[Path, str]:
    archive = ROOT / "stages/stage14/archive"
    hits = sorted(p for p in archive.glob("*.md") if token.lower() in p.name.lower())
    assert hits, f"missing archive artifact containing {token!r}"
    # One canonical matching artifact is enough for the boundary check.
    return hits[0], hits[0].read_text(encoding="utf-8")


def upstream_boundary_checks() -> dict:
    s5u = read("stages/stage14/14-s5u/result.md")
    assert "S5_METHOD_CLOSED=true" in s5u
    assert "ACTIVE_PHYSICAL_BASE_UPPER_BOUND_EXPONENT=41/42" in s5u
    assert "CURRENT_PROVED_SINGLE_EDGE_CEILING=1/20" in s5u

    p4ak, a4ak = find_archive("4ak")
    assert "PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTS=false" in a4ak
    assert "FIXED_CURVE_SQRTB_MECHANISM_REJECTED=true" in a4ak

    p4al, a4al = find_archive("4al")
    assert "COLLECTIVE_FIRST_HIT_IDENTITY_LOCKED=true" in a4al
    assert "SQRTB_EQUIVALENT_TO_INVERSE_SQRT_ACTIVATION_DENSITY=true" in a4al

    return {
        "s5u": "stages/stage14/14-s5u/result.md",
        "stage14_4ak": str(p4ak.relative_to(ROOT)),
        "stage14_4al": str(p4al.relative_to(ROOT)),
    }


def exponent_budget() -> dict:
    current = Fraction(41, 42)
    target = Fraction(1, 2)
    required = current - target
    assert required == Fraction(10, 21)

    # Sanity: any positive direct post-local exponent improves s5u.
    sample = Fraction(1, 100)
    assert current - sample < current
    assert current - required == target

    # Existing s5 micro-optimization ceiling is nowhere near sqrt(B).
    local_ceiling_physical = Fraction(39, 40)
    assert local_ceiling_physical > target
    assert current > local_ceiling_physical
    assert current - local_ceiling_physical == Fraction(1, 840)

    return {
        "current_physical_exponent": str(current),
        "sqrt_target_exponent": str(target),
        "required_post_local_saving": str(required),
        "current_s5_module_ceiling_physical": str(local_ceiling_physical),
        "remaining_s5_micro_gain_only": str(current - local_ceiling_physical),
    }


def route_matrix() -> dict:
    routes = {
        "local_only": {
            "primary": False,
            "reason": "closed s5 strength ceiling is far from 1/2",
        },
        "fixed_M4_bisection": {
            "primary": False,
            "reason": "theorem-level rejected by Stage14-4ak",
        },
        "rank_density": {
            "primary": False,
            "reason": "positive rank does not remove the physical first-small-point gate",
        },
        "separated_Sha_then_height": {
            "primary": False,
            "reason": "creates two unmatched moving-family theorems before any saving",
        },
        "direct_post_local_global_small_point_incidence": {
            "primary": True,
            "reason": "counts exactly the global + physical bounded-height event on supported 2-covers",
        },
    }
    assert sum(1 for x in routes.values() if x["primary"]) == 1
    assert routes["direct_post_local_global_small_point_incidence"]["primary"]
    return routes


def roadmap() -> list[dict]:
    rows = [
        ("s6-00", "architecture and exponent budget"),
        ("s6-01", "exact denominator-cleared global-small-point 2-cover incidence"),
        ("s6-02", "primitive box, torsion/boundary removal, support-prime split"),
        ("s6-03", "visible large-prime projective-incidence count"),
        ("s6-04", "Gaussian/dual kernel-invisible branch"),
        ("s6-05", "cover-conditioned smooth-support branch"),
        ("s6-06", "assemble first positive post-local retainer"),
        ("s6-07", "optimize/amplify versus 10/21 target"),
        ("s6-08", "sqrt upper-bound gate or isolate structural barrier"),
        ("s6-09", "close s6 package / next-method decision"),
    ]
    assert [x[0] for x in rows] == [f"s6-{i:02d}" for i in range(10)]
    return [{"stage": a, "role": b} for a, b in rows]


def main() -> None:
    report = {
        "metadata": {
            "stage": "14-s6-00",
            "classification": "ARCHITECTURE_AND_EXACT_EXPONENT_BUDGET",
        },
        "upstream": upstream_boundary_checks(),
        "exponent_budget": exponent_budget(),
        "routes": route_matrix(),
        "roadmap": roadmap(),
        "weapon_order": [
            "canonical_large_prime_projective_incidence",
            "Gaussian_dual_invisible_branch",
            "cover_conditioned_smooth_support",
            "determinant_or_square_sieve_only_after_exact_variety_audit",
        ],
    }
    print(json.dumps(report, indent=2, sort_keys=True))

    decisions = {
        "STAGE14_S6_00": "COMPLETE_POST_LOCAL_GLOBAL_SMALL_POINT_ARCHITECTURE",
        "S5_METHOD_ACCEPTED_AS_CLOSED": True,
        "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT": "41/42",
        "POST_LOCAL_SAVING_REQUIRED_FOR_SQRT_B_UPPER_BOUND": "10/21",
        "ANY_POSITIVE_POST_LOCAL_SAVING_IS_NEW_PROGRESS": True,
        "FIXED_M4_BISECTION_ROUTE_REOPEN": False,
        "LOCAL_SIEVE_CONTINUATION_PRIMARY": False,
        "RANK_DENSITY_PRIMARY": False,
        "SEPARATED_SHA_THEN_HEIGHT_PRIMARY": False,
        "DIRECT_POST_LOCAL_GLOBAL_SMALL_POINT_INCIDENCE_PRIMARY": True,
        "CANONICAL_LARGE_PRIME_INCIDENCE_FIRST_WEAPON": True,
        "GAUSSIAN_DUAL_INVISIBLE_BRANCH_RESERVED": True,
        "SMOOTH_SUPPORT_BRANCH_MUST_BE_COUNTED": True,
        "DETERMINANT_METHOD_IMPORT_UNCONDITIONAL": False,
        "S6_EXPECTED_DEFAULT_RANGE": "00..09",
        "S6_PREEMPTIVE_SUBSTAGE_SPLIT_REQUIRED": False,
        "SQRT_B_UPPER_BOUND_PROVED": False,
        "SQRT_B_ASYMPTOTIC_PROVED": False,
        "NEXT": "Stage14-s6-01",
    }
    for key, value in decisions.items():
        if isinstance(value, bool):
            value = str(value).lower()
        print(f"{key}={value}")


if __name__ == "__main__":
    main()
