#!/usr/bin/env python3
"""Stage13-3d: exact Stage12 representation/fiber bridge to canonical raw incidence.

The Stage12 primitive oriented construction uses a distinguished integral face

    x^2 + y^2 = p^2,    p^2 + z^2 = d^2,

with the first face ordered.  Stage13 raw incidence forgets that internal
ordering, sorts the three edges canonically, and retains the distinguished face.

This audit verifies at several finite cutoffs the exact combinatorial bridge
proved in Stage13-3d:

    C_prim(B) = 2 * (A_ab(B) + A_ac(B) + A_bc(B)).

More finely, after retaining the full orientation sigma, every supported fiber
has size 1 and each canonical face incidence has exactly two supported
orientations (the two orders of the distinguished face legs).
"""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

DEFAULT_BOUNDS = (1_000, 2_000, 5_000, 10_000, 20_000, 50_000, 100_000)
DEFAULT_OUTPUT = Path("stages/stage13/data/13-3/representation_fiber_report.json")

CATS = ("ab", "ac", "bc")
POS = ("a", "b", "c")
RAW_DIRECTION_LOCKS = {
    1_000: (306, 160, 138),
    2_000: (702, 372, 370),
    5_000: (2_300, 1_138, 1_077),
    10_000: (5_281, 2_740, 2_659),
    20_000: (12_407, 6_284, 6_105),
    50_000: (37_014, 19_080, 17_905),
    100_000: (84_212, 43_236, 40_760),
}
HISTORICAL_STAGE12_RAW_LOCKS = {
    1_000: 3_180,
    2_000: 8_396,
    5_000: 29_446,
    10_000: 74_414,
    20_000: 185_206,
}


def generate_pythagorean_indexes(bound: int):
    """All positive integer Pythagorean triples with hypotenuse <= bound.

    hyp[p] stores unordered positive face-leg pairs x<y with x^2+y^2=p^2.
    leg[p] stores (z,d) whenever p^2+z^2=d^2.
    """
    hyp: dict[int, list[tuple[int, int]]] = defaultdict(list)
    leg: dict[int, list[tuple[int, int]]] = defaultdict(list)

    for m in range(2, math.isqrt(bound) + 1):
        for n in range(1, m):
            if (m - n) % 2 == 0 or math.gcd(m, n) != 1:
                continue
            u = m * m - n * n
            v = 2 * m * n
            w = m * m + n * n
            if w > bound:
                continue
            if u > v:
                u, v = v, u

            k = 1
            while k * w <= bound:
                x, y, d = k * u, k * v, k * w
                hyp[d].append((x, y))
                leg[x].append((y, d))
                leg[y].append((x, d))
                k += 1

    return hyp, leg


def G(n: int) -> int:
    """Stage12 multiplicity G(n)=prod_{q|n,q=1 mod 4}(2 v_q(n)+1)."""
    x = n
    out = 1

    while x % 2 == 0:
        x //= 2

    q = 3
    while q * q <= x:
        if x % q == 0:
            e = 0
            while x % q == 0:
                x //= q
                e += 1
            if q % 4 == 1:
                out *= 2 * e + 1
        q += 2

    if x > 1 and x % 4 == 1:
        out *= 3

    return out


def category_and_orientation(
    ordered_face: tuple[int, int],
    complement: int,
    canonical_edges: tuple[int, int, int],
) -> tuple[str, str]:
    """Return canonical face category and Stage12 orientation word."""
    labels = {}
    for label, value in zip(POS, canonical_edges):
        labels[value] = label

    x, y = ordered_face
    face_labels = frozenset((labels[x], labels[y]))
    category = {
        frozenset(("a", "b")): "ab",
        frozenset(("a", "c")): "ac",
        frozenset(("b", "c")): "bc",
    }[face_labels]
    orientation = labels[x] + labels[y] + labels[complement]
    return category, orientation


def parity_type(face_values: tuple[int, int]) -> str:
    return "OE" if (face_values[0] & 1) != (face_values[1] & 1) else "EE"


def reconstruct_hyperbola(p: int, z: int, d: int) -> tuple[int, int, int]:
    """Recover the unique Stage12 (h,r,s) from p^2+z^2=d^2."""
    u = d - z
    v = d + z
    h = math.gcd(u, v)
    rr = u // h
    ss = v // h
    r = math.isqrt(rr)
    s = math.isqrt(ss)

    if not (
        r * r == rr
        and s * s == ss
        and r < s
        and math.gcd(r, s) == 1
        and p == h * r * s
        and z == h * (s * s - r * r) // 2
        and d == h * (r * r + s * s) // 2
    ):
        raise ArithmeticError(("hyperbola reconstruction failed", p, z, d, h, r, s))

    return h, r, s


def audit_bound(bound: int) -> dict[str, Any]:
    hyp, leg = generate_pythagorean_indexes(bound)

    g_identity_checks = 0
    for p, reps in hyp.items():
        g_identity_checks += 1
        if G(p) - 1 != 2 * len(reps):
            raise ArithmeticError(
                f"G identity failed at p={p}: G-1={G(p)-1}, ordered={2*len(reps)}"
            )

    stage12_raw_oriented = 0
    stage12_primitive_oriented = 0

    incidences: set[tuple[int, int, int, int, str]] = set()
    direction_incidence = Counter()
    direction_stage12_records = Counter()

    orientation_fibers = Counter()
    supported_orientation_count = Counter()

    parity_incidence = {kind: Counter() for kind in ("OE", "EE")}
    parity_records = {kind: Counter() for kind in ("OE", "EE")}

    hyperbola_checked: set[tuple[int, int, int]] = set()
    duplicate_incidence_gluings = 0

    for p, face_pairs in hyp.items():
        extensions = leg.get(p, ())
        if not extensions:
            continue

        for x, y in face_pairs:
            for z, d in extensions:
                if z == x or z == y:
                    raise ArithmeticError(("repeated edge", x, y, p, z, d))

                stage12_raw_oriented += 2

                if (p, z, d) not in hyperbola_checked:
                    reconstruct_hyperbola(p, z, d)
                    hyperbola_checked.add((p, z, d))

                if math.gcd(math.gcd(x, y), z) != 1:
                    continue

                stage12_primitive_oriented += 2
                canonical = tuple(sorted((x, y, z)))
                if not canonical[0] < canonical[1] < canonical[2]:
                    raise ArithmeticError(("canonical distinctness", x, y, z, d))

                cat, orientation1 = category_and_orientation((x, y), z, canonical)
                _, orientation2 = category_and_orientation((y, x), z, canonical)

                incidence = (*canonical, d, cat)
                if incidence in incidences:
                    duplicate_incidence_gluings += 1
                incidences.add(incidence)
                direction_incidence[cat] += 1

                ptype = parity_type((x, y))
                parity_incidence[ptype][cat] += 1

                for orientation in (orientation1, orientation2):
                    fiber_key = (incidence, orientation)
                    orientation_fibers[fiber_key] += 1
                    direction_stage12_records[cat] += 1
                    parity_records[ptype][cat] += 1

    if duplicate_incidence_gluings:
        raise ArithmeticError(f"duplicate incidence gluings: {duplicate_incidence_gluings}")

    for (incidence, _orientation), multiplicity in orientation_fibers.items():
        if multiplicity != 1:
            raise ArithmeticError(("nonunit supported fiber", incidence, multiplicity))
        supported_orientation_count[incidence] += 1

    if any(value != 2 for value in supported_orientation_count.values()):
        raise ArithmeticError("a canonical incidence did not have exactly two supported orientations")

    raw_vector = tuple(direction_incidence[c] for c in CATS)
    record_vector = tuple(direction_stage12_records[c] for c in CATS)

    if bound in RAW_DIRECTION_LOCKS and raw_vector != RAW_DIRECTION_LOCKS[bound]:
        raise ArithmeticError(
            f"Stage13 raw lock failed at B={bound}: {raw_vector} != {RAW_DIRECTION_LOCKS[bound]}"
        )

    if bound in HISTORICAL_STAGE12_RAW_LOCKS:
        expected = HISTORICAL_STAGE12_RAW_LOCKS[bound]
        if stage12_raw_oriented != expected:
            raise ArithmeticError(
                f"Stage12 raw lock failed at B={bound}: "
                f"{stage12_raw_oriented} != {expected}"
            )

    if stage12_primitive_oriented != 2 * len(incidences):
        raise ArithmeticError("primitive bridge total failed")

    if record_vector != tuple(2 * x for x in raw_vector):
        raise ArithmeticError("directional bridge failed")

    for kind in ("OE", "EE"):
        if any(parity_records[kind][c] != 2 * parity_incidence[kind][c] for c in CATS):
            raise ArithmeticError(("parity bridge failed", kind))

    return {
        "B": bound,
        "stage13_raw_incidence": dict(zip(CATS, raw_vector)),
        "stage13_raw_incidence_total": len(incidences),
        "stage12_projected_primitive_records": dict(zip(CATS, record_vector)),
        "stage12_primitive_oriented_total": stage12_primitive_oriented,
        "stage12_raw_oriented_total_all_scales": stage12_raw_oriented,
        "projection_ratio": stage12_primitive_oriented / len(incidences),
        "fiber_audit": {
            "supported_orientation_fibers": len(orientation_fibers),
            "fiber_size_histogram": {"1": len(orientation_fibers)},
            "supported_orientations_per_incidence_histogram": {"2": len(incidences)},
            "duplicate_incidence_gluings": duplicate_incidence_gluings,
            "hyperbola_extensions_checked": len(hyperbola_checked),
            "G_identity_values_checked": g_identity_checks,
        },
        "parity_control": {
            kind: {
                "incidence": {c: parity_incidence[kind][c] for c in CATS},
                "stage12_records": {c: parity_records[kind][c] for c in CATS},
                "projection_ratio": (
                    sum(parity_records[kind].values()) / sum(parity_incidence[kind].values())
                ),
            }
            for kind in ("OE", "EE")
        },
    }


def build_report(bounds: tuple[int, ...]) -> dict[str, Any]:
    rows = [audit_bound(bound) for bound in bounds]
    return {
        "metadata": {
            "stage": "13-3d",
            "title": "Exact Stage12 representation/fiber bridge after canonical projection",
            "counting_convention": (
                "Stage12 primitive oriented distinguished-face records projected to "
                "Stage13 primitive canonical raw face incidences"
            ),
            "bounds": list(bounds),
        },
        "exact_bridge": {
            "supported_full_orientation_fiber_size": 1,
            "supported_orientations_per_canonical_incidence": 2,
            "canonical_projection_multiplicity": 2,
            "identity": "C_prim(B)=2*(A_ab(B)+A_ac(B)+A_bc(B))",
            "directional_identity": "C_prim,uv^proj(B)=2*A_uv(B) for uv in {ab,ac,bc}",
            "parity_stratified_identity": (
                "the same factor 2 holds separately in OE and EE strata"
            ),
            "reason": (
                "G(p)-1 is the number of ordered positive face-leg representations; "
                "a fixed unordered distinguished face contributes exactly its two leg orders, "
                "while the complementary Pythagorean triple has a unique (h,r,s) parameterization"
            ),
        },
        "rows": rows,
        "conclusion": {
            "representation_fiber_is_direction_dependent": False,
            "representation_fiber_can_generate_or_flatten_direction_ratio": False,
            "stage12_total_raw_incidence_asymptotic": (
                "A_ab+A_ac+A_bc ~ kappa/(24*pi) * B*(log B)^3"
            ),
            "exact_one_bridge": (
                "N1=C_prim/2-2*(A_ab,ac+A_ab,bc+A_ac,bc)+3*A3"
            ),
            "overlap_negligibility_required_for_exact_one_asymptotic": True,
            "remaining_arithmetic_question": (
                "representation richness across different p values changes which distinct "
                "incidences exist, but it is not a variable fiber weight on a fixed incidence"
            ),
            "next": "Stage13-3e odd-prime / representation-density correction",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--bounds", nargs="+", type=int, default=list(DEFAULT_BOUNDS))
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    bounds = tuple(sorted(set(args.bounds)))
    if not bounds or bounds[0] <= 0:
        raise SystemExit("all bounds must be positive")

    report = build_report(bounds)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["conclusion"], indent=2))


if __name__ == "__main__":
    main()
