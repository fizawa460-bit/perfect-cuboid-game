#!/usr/bin/env python3
from __future__ import annotations

import json
import math
from collections import Counter, defaultdict
from pathlib import Path

OUT = Path("stages/stage14/data/14-e2/ambient_reconnaissance.json")
CUTOFFS = [2000, 10000, 50000, 200000, 1000000]
BOX_CUTOFFS = [1000, 10000, 100000]
OEIS_A239618 = {1000: 5, 10000: 19, 100000: 65}

LOCKED_TOTALS = {
    2000: (4812, (1342, 2136, 1334), 7),
    10000: (41666, (12464, 18198, 11004), 18),
    50000: (331731, (103892, 142403, 85436), 42),
    200000: (1896505, (612678, 805875, 477952), 82),
    1000000: (13817725, (4592536, 5816786, 3408403), 219),
}


def is_square(n: int) -> bool:
    r = math.isqrt(n)
    return r * r == n


def pythagorean_neighbors(hyp_limit: int):
    nbr = defaultdict(set)
    m = 2
    while m * m + 1 <= hyp_limit:
        for n in range(1, m):
            if math.gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            a = m * m - n * n
            b = 2 * m * n
            h = m * m + n * n
            if h > hyp_limit:
                continue
            for k in range(1, hyp_limit // h + 1):
                A, C = k * a, k * b
                nbr[A].add(C)
                nbr[C].add(A)
        m += 1
    return nbr


def direction(e: int, x: int, y: int) -> str:
    assert x < y
    if e < x:
        return "a"
    if e < y:
        return "b"
    return "c"


def real_height_census(B: int):
    nbr = pythagorean_neighbors(B)
    raw = Counter()
    exact = Counter()
    euler_bricks = set()
    B2 = B * B

    for e, others in nbr.items():
        vals = sorted(others)
        for i, x in enumerate(vals):
            ex = e * e + x * x
            if ex >= B2:
                continue
            y_max = math.isqrt(B2 - ex)
            for y in vals[i + 1 :]:
                if y > y_max:
                    break
                if math.gcd(math.gcd(e, x), y) != 1:
                    continue
                q = direction(e, x, y)
                raw[q] += 1
                if is_square(x * x + y * y):
                    euler_bricks.add(tuple(sorted((e, x, y))))
                else:
                    exact[q] += 1

    raw_total = sum(raw.values())
    exact_total = sum(exact.values())
    third_inc = raw_total - exact_total
    assert third_inc == 3 * len(euler_bricks)

    L = math.log(B)
    return {
        "B": B,
        "raw_directional": {q: raw[q] for q in "abc"},
        "raw_total": raw_total,
        "exactly_two_directional": {q: exact[q] for q in "abc"},
        "exactly_two_total": exact_total,
        "ambient_euler_brick_object_count": len(euler_bricks),
        "third_face_square_incidence_count": third_inc,
        "third_face_square_incidence_fraction": third_inc / raw_total,
        "direction_proportions": {q: exact[q] / exact_total for q in "abc"},
        "normalizations": {
            "E2_over_B": exact_total / B,
            "E2_over_B_log_B": exact_total / (B * L),
            "E2_over_B_log2_B": exact_total / (B * L**2),
            "E2_over_B_log3_B": exact_total / (B * L**3),
        },
    }


def boxed_euler_bricks(edge_bound: int) -> int:
    """OEIS A239618 convention: primitive a<b<c<edge_bound."""
    hyp_limit = math.isqrt(2 * edge_bound * edge_bound) + 1
    nbr = pythagorean_neighbors(hyp_limit)
    bricks = set()
    for e, others in nbr.items():
        if e >= edge_bound:
            continue
        vals = sorted(v for v in others if v < edge_bound)
        for i, x in enumerate(vals):
            for y in vals[i + 1 :]:
                if math.gcd(math.gcd(e, x), y) != 1:
                    continue
                if is_square(x * x + y * y):
                    bricks.add(tuple(sorted((e, x, y))))
    return len(bricks)


def main():
    rows = []
    previous = None
    for B in CUTOFFS:
        row = real_height_census(B)
        expected_total, expected_dir, expected_eb = LOCKED_TOTALS[B]
        got_dir = tuple(row["exactly_two_directional"][q] for q in "abc")
        assert row["exactly_two_total"] == expected_total
        assert got_dir == expected_dir
        assert row["ambient_euler_brick_object_count"] == expected_eb
        if previous is not None:
            row["effective_power_from_previous"] = math.log(
                row["exactly_two_total"] / previous["exactly_two_total"]
            ) / math.log(B / previous["B"])
        rows.append(row)
        previous = row

    box_observed = {B: boxed_euler_bricks(B) for B in BOX_CUTOFFS}
    assert box_observed == OEIS_A239618

    report = {
        "metadata": {
            "stage": "14-e2",
            "track": "front-side two-face ambient finite reconnaissance",
            "height": "D_R=sqrt(e^2+x^2+y^2)<=B",
            "integer_space_diagonal_required": False,
            "large_cutoff_method": "edge-first Pythagorean-neighbor enumeration",
            "e1_bijection_lock": "edge-first == face-pair-first through B=2000",
        },
        "cutoffs": rows,
        "external_census_crosscheck": {
            "source": "OEIS A239618 primitive Euler bricks under strict max-edge cutoff",
            "expected": {str(k): v for k, v in OEIS_A239618.items()},
            "observed": {str(k): v for k, v in box_observed.items()},
            "pass": True,
            "cutoff_note": "boxed max-edge height differs from Stage14-e real Euclidean height",
        },
        "finite_diagnostics": {
            "growth_candidate": "B*(log B)^3 is high-priority for e3 because its normalization is unusually stable on this finite range",
            "direction_observation": "b remains largest through B=1e6; a share rises and c share falls",
            "third_face_observation": "third-face-square incidence fraction shrinks strongly across the audited range",
            "claim_level": "finite diagnostics only",
        },
        "status": {
            "STAGE14_E2": "COMPLETE_FINITE_AMBIENT_RECONNAISSANCE",
            "MAX_RECON_B": 1000000,
            "OEIS_A239618_CROSSCHECK_PASS": True,
            "ASYMPTOTIC_CLAIM_MADE": False,
            "DIRECTIONAL_LIMIT_CLAIM_MADE": False,
            "LITERATURE_REFRESH_REQUIRED_AND_RECORDED": True,
            "NEXT_E_TASK": "Stage14-e3 total ambient growth with literature-first asymptotic collision audit",
        },
        "pass": True,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["status"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
