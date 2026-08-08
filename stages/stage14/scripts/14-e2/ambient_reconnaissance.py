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
    2000: (4812, (1342, 2136, 1334), 4833, 7),
    10000: (41666, (12464, 18198, 11004), 41720, 18),
    50000: (331731, (103892, 142403, 85436), 331857, 42),
    200000: (1896505, (612678, 805875, 477952), 1896751, 82),
    1000000: (13817725, (4592536, 5816786, 3408403), 13818382, 219),
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
            a, b, h = m * m - n * n, 2 * m * n, m * m + n * n
            if h > hyp_limit:
                continue
            for k in range(1, hyp_limit // h + 1):
                A, C = k * a, k * b
                nbr[A].add(C)
                nbr[C].add(A)
        m += 1
    return nbr


def direction(e: int, x: int, y: int) -> str:
    if e < x:
        return "a"
    if e < y:
        return "b"
    return "c"


def real_height_census(B: int):
    nbr = pythagorean_neighbors(B)
    raw, exact = Counter(), Counter()
    bricks = set()
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
                    bricks.add(tuple(sorted((e, x, y))))
                else:
                    exact[q] += 1
    raw_total = sum(raw.values())
    exact_total = sum(exact.values())
    assert raw_total - exact_total == 3 * len(bricks)
    return raw_total, exact_total, tuple(exact[q] for q in "abc"), len(bricks)


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
    final_direction = None
    final_third_fraction = None
    for B in CUTOFFS:
        raw_total, E2, dirs, bricks = real_height_census(B)
        expected_E2, expected_dirs, expected_raw, expected_bricks = LOCKED_TOTALS[B]
        assert (E2, dirs, raw_total, bricks) == (
            expected_E2,
            expected_dirs,
            expected_raw,
            expected_bricks,
        )
        logB = math.log(B)
        rows.append({
            "B": B,
            "exactly_two": list(dirs),
            "E2": E2,
            "raw_total": raw_total,
            "euler_bricks": bricks,
            "E2_over_B_log3_B": E2 / (B * logB**3),
        })
        if B == CUTOFFS[-1]:
            final_direction = [d / E2 for d in dirs]
            final_third_fraction = (raw_total - E2) / raw_total

    box_observed = {B: boxed_euler_bricks(B) for B in BOX_CUTOFFS}
    assert box_observed == OEIS_A239618

    report = {
        "stage": "14-e2",
        "height": "D_R=sqrt(e^2+x^2+y^2)<=B",
        "integer_space_diagonal_required": False,
        "cutoffs": rows,
        "oeis_A239618_crosscheck": {
            "strict_max_edge_cutoff": {str(k): v for k, v in box_observed.items()},
            "pass": True,
            "note": "different height convention; validates only the all-three-face Euler-brick subpopulation",
        },
        "finite_diagnostics_only": {
            "B_log3_candidate_priority": "high",
            "direction_at_B_1000000": final_direction,
            "third_face_square_incidence_fraction_at_B_1000000": final_third_fraction,
            "asymptotic_claim": False,
            "directional_limit_claim": False,
        },
        "status": {
            "STAGE14_E2": "COMPLETE_FINITE_AMBIENT_RECONNAISSANCE",
            "MAX_RECON_B": 1000000,
            "LITERATURE_REFRESH_RECORDED": True,
            "NEXT_E_TASK": "Stage14-e3 total ambient growth",
        },
        "pass": True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report["status"], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
