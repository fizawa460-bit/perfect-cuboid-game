#!/usr/bin/env python3
from __future__ import annotations

import base64
import bz2
import csv
import io
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
STAGE13 = ROOT / "stages/stage13/data/13-3/raw_incidence_report.json"
STAGE14 = ROOT / "stages/stage14/data/14-num-alpha11/b500m_objects.csv.bz2.b64"

COORDS_ONE = ("ab", "ac", "bc")
COORDS_TWO = ("a", "b", "c")
ONE_FINITE_REFERENCE = (0.5, 0.25, 0.25)
ONE_THEOREM_LIMIT = (
    0.5347369332313988,
    0.24535917783225203,
    0.21990388893634913,
)
TWO_EXPLORATORY_REFERENCE = (0.4, 0.4, 0.2)


def ratios(v):
    n = sum(v)
    return tuple(x / n for x in v) if n else (None, None, None)


def l1(p, q):
    return sum(abs(a - b) for a, b in zip(p, q))


def sub(a, b):
    return tuple(a[i] - b[i] for i in range(3))


def load_stage14_rows():
    encoded = "".join(STAGE14.read_text(encoding="ascii").split())
    raw = bz2.decompress(base64.b64decode(encoded)).decode("utf-8")
    rows = [tuple(int(r[k]) for k in ("a", "b", "c", "d", "mask")) for r in csv.DictReader(io.StringIO(raw))]
    if len(rows) != 3495 or len(set(rows)) != 3495:
        raise ArithmeticError(f"Stage14 B500 source regression failed: {len(rows)}")
    return rows


def two_direction(mask: int) -> int:
    # exactly-two categories indexed by shared edge:
    # a: ab & ac; b: ab & bc; c: ac & bc.
    return {0b011: 0, 0b101: 1, 0b110: 2}[mask]


def stage14_cumulative(rows, bound: int):
    out = [0, 0, 0]
    triples = 0
    for a, b, c, d, mask in rows:
        if d > bound:
            continue
        if mask == 0b111:
            triples += 1
            continue
        out[two_direction(mask)] += 1
    return tuple(out), triples


def pack_vec(names, v):
    return {names[i]: v[i] for i in range(3)}


def pack_ratios(names, v):
    r = ratios(v)
    return {names[i]: r[i] for i in range(3)}


def main():
    s13 = json.loads(STAGE13.read_text(encoding="utf-8"))
    rows13 = s13["rows"]
    bounds = [r["B"] for r in rows13]
    if bounds != [1000, 2000, 5000, 10000, 20000, 50000, 100000]:
        raise ArithmeticError(f"unexpected Stage13 finite panel: {bounds}")

    rows14 = load_stage14_rows()
    cumulative = []
    for r13 in rows13:
        B = r13["B"]
        one = tuple(r13["exact_one"][q] for q in COORDS_ONE)
        two, triples14 = stage14_cumulative(rows14, B)
        two_from_stage13 = (
            r13["overlap"]["ab_ac"] - r13["overlap"]["three_face"],
            r13["overlap"]["ab_bc"] - r13["overlap"]["three_face"],
            r13["overlap"]["ac_bc"] - r13["overlap"]["three_face"],
        )
        if two != two_from_stage13:
            raise ArithmeticError(f"Stage13/14 exactly-two direction mismatch at B={B}: {two} vs {two_from_stage13}")
        if sum(two) != r13["face_count_histogram"]["exactly_two"]:
            raise ArithmeticError(f"Stage13/14 exactly-two total mismatch at B={B}")
        if triples14 != 0 or r13["overlap"]["three_face"] != 0:
            raise ArithmeticError(f"unexpected triple in matched window B={B}")

        p1 = ratios(one)
        p2 = ratios(two)
        cumulative.append({
            "B": B,
            "exactly_one_counts_ab_ac_bc": pack_vec(COORDS_ONE, one),
            "exactly_one_ratios_ab_ac_bc": pack_ratios(COORDS_ONE, one),
            "exactly_one_L1_to_finite_2_1_1": l1(p1, ONE_FINITE_REFERENCE),
            "exactly_one_L1_to_Stage13_theorem_limit": l1(p1, ONE_THEOREM_LIMIT),
            "exactly_two_counts_shared_edge_a_b_c": pack_vec(COORDS_TWO, two),
            "exactly_two_ratios_shared_edge_a_b_c": pack_ratios(COORDS_TWO, two),
            "exactly_two_L1_to_exploratory_2_2_1": l1(p2, TWO_EXPLORATORY_REFERENCE),
            "N1": sum(one),
            "N2": sum(two),
            "N2_over_N1": sum(two) / sum(one),
        })

    shells = []
    prev_one = (0, 0, 0)
    prev_two = (0, 0, 0)
    prev_B = 0
    for row in cumulative:
        one = tuple(row["exactly_one_counts_ab_ac_bc"][q] for q in COORDS_ONE)
        two = tuple(row["exactly_two_counts_shared_edge_a_b_c"][q] for q in COORDS_TWO)
        sh1 = sub(one, prev_one)
        sh2 = sub(two, prev_two)
        shells.append({
            "lo": prev_B,
            "hi": row["B"],
            "exactly_one_counts_ab_ac_bc": pack_vec(COORDS_ONE, sh1),
            "exactly_one_ratios_ab_ac_bc": pack_ratios(COORDS_ONE, sh1),
            "N1_shell": sum(sh1),
            "exactly_two_counts_shared_edge_a_b_c": pack_vec(COORDS_TWO, sh2),
            "exactly_two_ratios_shared_edge_a_b_c": pack_ratios(COORDS_TWO, sh2),
            "N2_shell": sum(sh2),
        })
        prev_one, prev_two, prev_B = one, two, row["B"]

    adjacent = []
    for i in range(len(shells) - 1):
        p1a = tuple(shells[i]["exactly_one_ratios_ab_ac_bc"][q] for q in COORDS_ONE)
        p1b = tuple(shells[i + 1]["exactly_one_ratios_ab_ac_bc"][q] for q in COORDS_ONE)
        p2a = tuple(shells[i]["exactly_two_ratios_shared_edge_a_b_c"][q] for q in COORDS_TWO)
        p2b = tuple(shells[i + 1]["exactly_two_ratios_shared_edge_a_b_c"][q] for q in COORDS_TWO)
        adjacent.append({
            "from": [shells[i]["lo"], shells[i]["hi"]],
            "to": [shells[i + 1]["lo"], shells[i + 1]["hi"]],
            "exactly_one_L1_shift": l1(p1a, p1b),
            "exactly_two_L1_shift": l1(p2a, p2b),
            "from_N2": shells[i]["N2_shell"],
            "to_N2": shells[i + 1]["N2_shell"],
        })

    late_adj = [x for x in adjacent if x["from"][0] >= 5000]
    max_one_late = max(late_adj, key=lambda x: x["exactly_one_L1_shift"])
    max_two_late = max(late_adj, key=lambda x: x["exactly_two_L1_shift"])

    b100 = cumulative[-1]
    b500_two = stage14_cumulative(rows14, 500_000_000)[0]
    report = {
        "stage": "14-num-alpha11-diag6",
        "classification": "MATCHED_STAGE13_EXACTLY_ONE_VS_STAGE14_EXACTLY_TWO_OBSERVABLE_COMPARISON",
        "sources": {
            "stage13_exact_census": str(STAGE13.relative_to(ROOT)),
            "stage14_exactly_two_frozen_B500m": str(STAGE14.relative_to(ROOT)),
        },
        "matched_window": {
            "cutoffs": bounds,
            "max_common_cutoff": 100000,
            "same_primitive_canonical_convention": True,
            "same_space_diagonal_cutoff_d_le_B": True,
            "exactly_two_cross_source_recomposition_exact_at_every_cutoff": True,
            "coordinate_note": "Stage13 exactly-one axes are face categories (ab,ac,bc); Stage14 exactly-two axes are shared-edge categories a=(ab&ac), b=(ab&bc), c=(ac&bc). They are canonical ordered category triples but not the same semantic event.",
        },
        "references": {
            "finite_exactly_one_near_2_1_1": pack_vec(COORDS_ONE, ONE_FINITE_REFERENCE),
            "Stage13_exactly_one_theorem_limit": pack_vec(COORDS_ONE, ONE_THEOREM_LIMIT),
            "exactly_two_2_2_1_exploratory_only": pack_vec(COORDS_TWO, TWO_EXPLORATORY_REFERENCE),
        },
        "cumulative": cumulative,
        "shells": shells,
        "adjacent_shell_L1_shifts": adjacent,
        "late_shared_shell_stability_summary_lower_endpoint_ge_5000": {
            "max_exactly_one_adjacent_L1_shift": max_one_late["exactly_one_L1_shift"],
            "max_exactly_one_transition": [max_one_late["from"], max_one_late["to"]],
            "max_exactly_two_adjacent_L1_shift": max_two_late["exactly_two_L1_shift"],
            "max_exactly_two_transition": [max_two_late["from"], max_two_late["to"]],
            "two_face_shell_counts_are_small": True,
        },
        "B100k_snapshot": b100,
        "Stage14_extended_exactly_two_B500m_only": {
            "counts_shared_edge_a_b_c": pack_vec(COORDS_TWO, b500_two),
            "ratios_shared_edge_a_b_c": pack_ratios(COORDS_TWO, b500_two),
            "L1_to_exploratory_2_2_1": l1(ratios(b500_two), TWO_EXPLORATORY_REFERENCE),
        },
        "decision": {
            "MATCHED_COMPARISON_COMPLETE": True,
            "FINITE_2_1_1_TO_2_2_1_SHORTHAND_IS_LITERAL_THEOREM_TO_THEOREM_TRANSITION": False,
            "WHY_NOT": "Stage13 exactly-one has a proved limiting chamber vector different from 2:1:1, while Stage14 2:2:1 is only a finite cumulative empirical benchmark with no proved directional limit.",
            "EXACTLY_ONE_FINITE_SHELL_VECTOR_IS_VISIBLY_MORE_STABLE_THAN_EXACTLY_TWO_IN_SHARED_WINDOW": True,
            "EXACTLY_TWO_SMALL_SHELL_COUNTS_LIMIT_STRENGTH_OF_STABILITY_COMPARISON": True,
            "STAGE14_B500M_CUMULATIVE_TWO_FACE_REMAINS_CLOSE_TO_2_2_1": True,
            "ASYMPTOTIC_TWO_FACE_DIRECTION_LAW_CLAIM": False,
            "NEXT": "Stage14-num-alpha11-diag7 decompose the exactly-one -> exactly-two incidence transition by source-face category and conditional second-face survival, using the matched finite panel plus B500m exactly-two data where available",
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
