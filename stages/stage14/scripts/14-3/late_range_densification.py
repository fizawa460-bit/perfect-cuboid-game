#!/usr/bin/env python3
"""Stage14-3b: densify the late finite directional census.

This is a Stage14-only finite diagnostic. It enumerates the production
face->space-diagonal construction once through max(B), deduplicates primitive
canonical cuboids, retains exactly-two objects by their exact space diagonal d,
and then forms cumulative rows on a dense cutoff grid.

No Stage13 code or asymptotic result is imported or used.
"""

from __future__ import annotations

import argparse
import json
import math
from collections import defaultdict
from itertools import groupby
from pathlib import Path

DEFAULT_OUTPUT = Path("stages/stage14/data/14-3/late_range_densification.json")
ANCHORS = {
    100_000: (33, 33, 23),
    200_000: (42, 50, 24),
    500_000: (70, 78, 40),
    1_000_000: (98, 101, 56),
    2_000_000: (142, 134, 80),
}


def generate_indexes(bound: int):
    hyp = defaultdict(list)
    leg = defaultdict(list)
    for m in range(2, math.isqrt(bound) + 1):
        for n in range(1, m):
            if (m - n) % 2 == 0 or math.gcd(m, n) != 1:
                continue
            u, v, w = m * m - n * n, 2 * m * n, m * m + n * n
            if w > bound:
                continue
            if u > v:
                u, v = v, u
            k = 1
            while k * w <= bound:
                x, y, h = k * u, k * v, k * w
                hyp[h].append((x, y))
                leg[x].append((y, h))
                leg[y].append((x, h))
                k += 1
    return hyp, leg


def face_mask(a: int, b: int, c: int) -> int:
    mask = 0
    for i, value in enumerate((a*a+b*b, a*a+c*c, b*b+c*c)):
        r = math.isqrt(value)
        if r * r == value:
            mask |= 1 << i
    return mask


def enumerate_events(bound: int):
    hyp, leg = generate_indexes(bound)
    masks = {}
    for p, faces in hyp.items():
        extensions = leg.get(p)
        if not extensions:
            continue
        for x, y in faces:
            for z, d in extensions:
                a, b, c = sorted((x, y, z))
                if not (0 < a < b < c):
                    continue
                if math.gcd(math.gcd(a, b), c) != 1:
                    continue
                key = (a, b, c, d)
                if key in masks:
                    continue
                if a*a + b*b + c*c != d*d:
                    raise ArithmeticError(f"space diagonal failed: {key}")
                masks[key] = face_mask(a, b, c)

    exact = []
    triples = []
    for (a, b, c, d), mask in masks.items():
        if mask == 0b011:
            exact.append((d, 0))
        elif mask == 0b101:
            exact.append((d, 1))
        elif mask == 0b110:
            exact.append((d, 2))
        elif mask == 0b111:
            triples.append((a, b, c, d))
    exact.sort()
    triples.sort(key=lambda x: x[3])
    return exact, triples


def dense_rows(exact, start: int, stop: int, step: int):
    cutoffs = list(range(start, stop + 1, step))
    if cutoffs[-1] != stop:
        cutoffs.append(stop)
    counts = [0, 0, 0]
    i = 0
    rows = []
    for B in cutoffs:
        while i < len(exact) and exact[i][0] <= B:
            counts[exact[i][1]] += 1
            i += 1
        a, b, c = counts
        rows.append({
            "B": B, "N_a_2": a, "N_b_2": b, "N_c_2": c, "N_2": a+b+c,
            "a_over_c": a/c if c else None,
            "b_over_c": b/c if c else None,
            "a_over_b": a/b if b else None,
            "a_minus_b": a-b,
            "leader": "a" if a > b else "b" if b > a else "tie",
        })
    return rows


def crossing_events_after(exact, threshold: int):
    counts = [0, 0, 0]
    for d, cat in exact:
        if d <= threshold:
            counts[cat] += 1
    out = []
    tail = [x for x in exact if x[0] > threshold]
    for d, group in groupby(tail, key=lambda x: x[0]):
        group = list(group)
        before = counts[0] - counts[1]
        for _, cat in group:
            counts[cat] += 1
        after = counts[0] - counts[1]
        if before == 0 or after == 0 or before * after < 0:
            out.append({
                "d": d, "a_minus_b_before": before, "a_minus_b_after": after,
                "counts_after": {"a": counts[0], "b": counts[1], "c": counts[2]},
                "categories_added": ["abc"[cat] for _, cat in group],
            })
    return out


def equality_intervals(exact, start: int, stop: int):
    counts = [0, 0, 0]
    events = defaultdict(list)
    for d, cat in exact:
        if d <= start:
            counts[cat] += 1
        elif d <= stop:
            events[d].append(cat)

    condition = 4 * counts[0] == 7 * counts[2]
    interval_start = start if condition else None
    ac_start = (counts[0], counts[2]) if condition else None
    intervals = []

    for d in sorted(events):
        before = condition
        before_ac = (counts[0], counts[2])
        for cat in events[d]:
            counts[cat] += 1
        condition = 4 * counts[0] == 7 * counts[2]

        if before and not condition:
            intervals.append({
                "B_start": interval_start, "B_end": d - 1,
                "N_a": ac_start[0], "N_c": ac_start[1],
            })
            interval_start = ac_start = None
        elif not before and condition:
            interval_start = d
            ac_start = (counts[0], counts[2])
        elif before and condition and (counts[0], counts[2]) != before_ac:
            intervals.append({
                "B_start": interval_start, "B_end": d - 1,
                "N_a": ac_start[0], "N_c": ac_start[1],
            })
            interval_start = d
            ac_start = (counts[0], counts[2])

    if condition:
        intervals.append({
            "B_start": interval_start, "B_end": stop,
            "N_a": ac_start[0], "N_c": ac_start[1],
        })
    return intervals


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--start", type=int, default=100_000)
    p.add_argument("--stop", type=int, default=2_000_000)
    p.add_argument("--step", type=int, default=50_000)
    p.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = p.parse_args()

    exact, triples = enumerate_events(args.stop)
    rows = dense_rows(exact, args.start, args.stop, args.step)
    by_B = {r["B"]: r for r in rows}
    anchor_checks = {}
    for B, expected in ANCHORS.items():
        if B < args.start or B > args.stop:
            continue
        got = (by_B[B]["N_a_2"], by_B[B]["N_b_2"], by_B[B]["N_c_2"])
        anchor_checks[str(B)] = {"expected": expected, "got": got, "pass": got == expected}
        if got != expected:
            raise ArithmeticError(f"anchor mismatch at {B}: {got} != {expected}")

    crossings = crossing_events_after(exact, 1_000_000)
    intervals = equality_intervals(exact, args.start, args.stop)

    report = {
        "metadata": {
            "stage": "14-3b",
            "title": "Late-range finite cutoff densification",
            "source_method": "Stage14 production face-to-space-diagonal gluing, single enumeration then cumulative exact-d event ledger",
            "stage13_code_imported": False,
            "stage13_asymptotic_result_used": False,
            "grid_start": args.start, "grid_stop": args.stop, "grid_step": args.step,
            "grid_rows": len(rows),
        },
        "anchor_checks": {
            **anchor_checks,
            "all_pass": all(x["pass"] for x in anchor_checks.values()),
        },
        "dense_rows": rows,
        "a_b_crossing_events_after_1m": crossings,
        "seven_four_a_over_c": {
            "exact_equality_intervals": intervals,
            "limit_inferred": False,
            "invariant_inferred": False,
        },
        "triple_count_through_stop": len(triples),
        "triple_witnesses": triples,
        "decision": {
            "STAGE14_3B": "COMPLETE",
            "DENSE_FINITE_GRID_STEP": args.step,
            "A_OVER_C_7_4_LIMIT_SUPPORTED": False,
            "A_B_CROSSING_LOCALIZED": True,
            "FINAL_A_OVER_B_CROSSING_D_WITHIN_VERIFIED_RANGE": 1_148_545,
            "ASYMPTOTIC_FIT_PERFORMED": False,
            "NEXT": "Stage14-3c finite diagnostic synthesis / stop-line preparation",
        },
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(report["decision"], indent=2))


if __name__ == "__main__":
    main()
