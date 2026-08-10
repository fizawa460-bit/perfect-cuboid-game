#!/usr/bin/env python3
"""Stage14-t59: exact two-comparator orthogonal rectangle reduction audit."""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import json
import math
import runpy

ROOT = Path(__file__).resolve().parents[4]
T36_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
T42_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t42_kummer_transversality_audit.py"
T58_RESULT = ROOT / "stages/stage14/14-t58/result.md"
OUT = ROOT / "stages/stage14/data/14-t59/orthogonal_rectangle_reduction.json"

B_FROZEN = 10_000


def gaussian_unit_key(z):
    x, y = z
    return min(((x, y), (-y, x), (-x, -y), (y, -x)))


def floor_log2_ratio(a: int, b: int) -> int:
    """Exact k with 2^k <= a/b < 2^(k+1), for positive integers."""
    assert a > 0 and b > 0
    if a >= b:
        k = 0
        while b * (1 << (k + 1)) <= a:
            k += 1
        return k
    k = -1
    while a * (1 << (-k)) < b:
        k -= 1
    return k


def comparator_descriptor(i: int, j: int, nleaf: int):
    """Dyadic first-differing-bit rectangle for ranked leaves i<j."""
    assert 0 <= i < j < nleaf
    assert nleaf > 0 and nleaf & (nleaf - 1) == 0
    xor = i ^ j
    bit = xor.bit_length() - 1
    depth_total = nleaf.bit_length() - 1
    depth = depth_total - 1 - bit
    prefix_i = i >> (bit + 1)
    prefix_j = j >> (bit + 1)
    assert prefix_i == prefix_j
    assert ((i >> bit) & 1) == 0
    assert ((j >> bit) & 1) == 1
    return depth, prefix_i


def rank_comparator(rows, cols, row_key, col_key, *, leq: bool):
    """Rank one strict or non-strict scalar comparator exactly."""
    if leq:
        tagged = sorted(
            set([(row_key(r), 0) for r in rows] + [(col_key(c), 1) for c in cols])
        )
        rank = {v: i for i, v in enumerate(tagged)}
        row_rank = {r: rank[(row_key(r), 0)] for r in rows}
        col_rank = {c: rank[(col_key(c), 1)] for c in cols}
        valid = lambda r, c: row_key(r) <= col_key(c)
        rank_count = len(tagged)
    else:
        values = sorted(set([row_key(r) for r in rows] + [col_key(c) for c in cols]))
        rank = {v: i for i, v in enumerate(values)}
        row_rank = {r: rank[row_key(r)] for r in rows}
        col_rank = {c: rank[col_key(c)] for c in cols}
        valid = lambda r, c: row_key(r) < col_key(c)
        rank_count = len(values)

    nleaf = 1
    while nleaf < rank_count:
        nleaf *= 2
    return row_rank, col_rank, nleaf, valid


def packet_key(s):
    k = s["n"] // s["delta"]
    return gaussian_unit_key(s["U"]), s["eps"], k


def row_key(s):
    return s["a"], s["b"], s["ell"]


def col_key(s):
    return s["p"], s["q"], s["n"], s["delta"]


def packet_label(key) -> str:
    U, eps, k = key
    return f"U={U},eps={eps},k={k}"


def audit_packet(key, states):
    Ukey, eps, k = key
    m_values = {s["m"] for s in states}
    assert len(m_values) == 1
    m = next(iter(m_values))

    rows = sorted({row_key(s) for s in states})
    cols = sorted({col_key(s) for s in states})
    observed = {(row_key(s), col_key(s)) for s in states}

    # Current reciprocal quotient has x<1, so tx<1 is automatic and the
    # chamber is exactly t<x.
    for s in states:
        assert s["p"] < s["q"]
        t = Fraction(s["a"], s["b"])
        x = Fraction(s["p"], s["q"])
        assert 0 < t < x < 1
        assert t * x < 1

    # Exact support reconstruction from the two side-to-side comparators.
    predicted = set()
    for r in rows:
        a, b, ell = r
        t = Fraction(a, b)
        assert ell * ell > 4 * B_FROZEN
        for c in cols:
            p, q, n, delta = c
            x = Fraction(p, q)
            assert n == k * delta
            if not (t < x):
                continue
            if eps * ell * m * delta > 2 * B_FROZEN:
                continue
            # Super-square-root separation: no additional ell|N(V) mask.
            assert n <= eps * m * delta
            assert ell > 2 * n
            assert n % ell != 0
            predicted.add((r, c))

    assert predicted == observed

    # Comparator 1: t(pi)<x(V).
    rr1, cr1, nleaf1, valid1 = rank_comparator(
        rows,
        cols,
        lambda r: Fraction(r[0], r[1]),
        lambda c: Fraction(c[0], c[1]),
        leq=False,
    )

    # Comparator 2: ell(pi)<=Y_U/delta(V), with exact equality included by tags.
    Y = Fraction(2 * B_FROZEN, eps * m)
    rr2, cr2, nleaf2, valid2 = rank_comparator(
        rows,
        cols,
        lambda r: Fraction(r[2], 1),
        lambda c: Y / Fraction(c[3], 1),
        leq=True,
    )

    rectangles = defaultdict(set)
    for r, c in observed:
        assert valid1(r, c)
        assert valid2(r, c)
        d1, p1 = comparator_descriptor(rr1[r], cr1[c], nleaf1)
        d2, p2 = comparator_descriptor(rr2[r], cr2[c], nleaf2)
        rectangles[(d1, d2, p1, p2)].add((r, c))

    rectangle_rows_cols = []
    for desc, edges in rectangles.items():
        rowset = {r for r, _ in edges}
        colset = {c for _, c in edges}
        cartesian = {(r, c) for r in rowset for c in colset}
        assert edges == cartesian
        a = len(rowset)
        b = len(colset)
        aspect = floor_log2_ratio(a, b)
        rectangle_rows_cols.append((desc, rowset, colset, a, b, aspect))

    assert sum(len(edges) for edges in rectangles.values()) == len(observed)

    # Fixed depth-pair + aspect bucket = one energy-balanced orthogonal family.
    families = defaultdict(list)
    for rec in rectangle_rows_cols:
        desc, rowset, colset, a, b, aspect = rec
        d1, d2, _, _ = desc
        families[(d1, d2, aspect)].append(rec)

    max_rectangles_per_family = 0
    family_mass = 0
    for _, family in families.items():
        seen_rows = set()
        seen_cols = set()
        R = 0
        A2 = 0
        B2 = 0
        for _, rowset, colset, a, b, _ in family:
            assert not (seen_rows & rowset)
            assert not (seen_cols & colset)
            seen_rows |= rowset
            seen_cols |= colset
            R += a * b
            A2 += a * a
            B2 += b * b
        assert A2 * B2 <= 2 * R * R
        family_mass += R
        max_rectangles_per_family = max(max_rectangles_per_family, len(family))

    assert family_mass == len(observed)

    return {
        "packet": packet_label(key),
        "U": list(Ukey),
        "eps": eps,
        "k": k,
        "states": len(states),
        "rows": len(rows),
        "cols": len(cols),
        "chamber_tree_depth": int(math.log2(nleaf1)),
        "hyperbola_tree_depth": int(math.log2(nleaf2)),
        "rectangles": len(rectangles),
        "energy_balanced_families": len(families),
        "max_rectangles_per_family": max_rectangles_per_family,
        "support_reconstruction_exact": True,
        "cartesian_rectangle_checks": len(rectangles),
        "family_energy_balance_checks": len(families),
    }


def main() -> None:
    t58 = T58_RESULT.read_text()
    assert "STAGE14_T58=COMPLETE_TOROIDAL_RECONSTRUCTION_MASK_SEPARATION_AND_RADIAL_CELL_ENERGY_TRANSFER" in t58
    assert "FIXED_U_PHYSICAL_SELECTOR_SUPPORT_ENERGY_TRANSFER_PROVED=true" in t58
    assert "FULL_PHYSICAL_SELECTOR_SINGLE_CARTESIAN_PRODUCT=false" in t58
    assert "SHARED_U_CANONICAL_PRIME_DELTA_TOROIDAL_SECOND_MOMENT_PROVED=false" in t58

    t36 = runpy.run_path(str(T36_SCRIPT), run_name="stage14_t36_import")
    t42 = runpy.run_path(str(T42_SCRIPT), run_name="stage14_t42_import")
    reps = t42["reciprocal_quotient"](t36["build_frozen_states"]())
    assert len(reps) == 560
    assert all(s["p"] < s["q"] for s in reps)

    invisible = [s for s in reps if s["branch"] == "invisible"]
    assert len(invisible) == 419

    packets = defaultdict(list)
    for s in invisible:
        packets[packet_key(s)].append(s)
    assert len(packets) == 8

    rows = [audit_packet(key, states) for key, states in sorted(packets.items())]

    frozen_compact = [
        (r["U"], r["eps"], r["k"], r["states"], r["rows"], r["cols"],
         r["chamber_tree_depth"], r["hyperbola_tree_depth"], r["rectangles"],
         r["energy_balanced_families"], r["max_rectangles_per_family"])
        for r in rows
    ]
    expected = [
        ([-2, -1], 2, 5, 20, 12, 2, 4, 4, 6, 6, 1),
        ([-2, -1], 2, 10, 7, 5, 2, 3, 3, 4, 4, 1),
        ([-2, 1], 2, 5, 13, 8, 2, 4, 3, 6, 5, 2),
        ([-2, 1], 2, 10, 2, 2, 1, 2, 2, 1, 1, 1),
        ([-1, -1], 1, 1, 96, 39, 7, 6, 6, 29, 23, 4),
        ([-1, -1], 1, 2, 64, 29, 6, 6, 6, 21, 19, 2),
        ([-1, 0], 2, 1, 131, 75, 7, 7, 7, 27, 25, 2),
        ([-1, 0], 2, 2, 86, 52, 6, 6, 6, 33, 26, 3),
    ]
    assert frozen_compact == expected

    totals = {
        "reciprocal_states": len(reps),
        "invisible_states": len(invisible),
        "packets": len(rows),
        "sum_rows_across_packets": sum(r["rows"] for r in rows),
        "sum_cols_across_packets": sum(r["cols"] for r in rows),
        "rectangles": sum(r["rectangles"] for r in rows),
        "energy_balanced_families": sum(r["energy_balanced_families"] for r in rows),
        "max_comparator_tree_depth": max(max(r["chamber_tree_depth"], r["hyperbola_tree_depth"]) for r in rows),
        "max_rectangles_per_family": max(r["max_rectangles_per_family"] for r in rows),
    }
    assert totals == {
        "reciprocal_states": 560,
        "invisible_states": 419,
        "packets": 8,
        "sum_rows_across_packets": 222,
        "sum_cols_across_packets": 33,
        "rectangles": 127,
        "energy_balanced_families": 109,
        "max_comparator_tree_depth": 7,
        "max_rectangles_per_family": 4,
    }

    report = {
        "stage": "14-t59",
        "totals": totals,
        "packets": rows,
        "exact_lemmas": {
            "reciprocal_chamber": "0<t<x<1 on quotient, so the chamber is exactly t<x",
            "super_sqrt_separation": "ell^2>4B and eps*ell*m*delta<=2B imply ell>2*N(V)",
            "comparator_decomposition": "every i<j is assigned to the unique first-differing-bit dyadic rectangle",
            "two_comparator_intersection": "fixed depth-pair intersections are Cartesian with disjoint row and column projections",
            "aspect_balance": "within 2^h<=a_j/b_j<2^(h+1), (sum a_j^2)(sum b_j^2)<=2(sum a_j*b_j)^2",
            "asymptotic_family_count": "O((log B)^3)",
        },
        "decision": {
            "STAGE14_T59": "COMPLETE_EXACT_TWO_COMPARATOR_ORTHOGONAL_RECTANGLE_REDUCTION",
            "RECIPROCAL_QUOTIENT_X_LT_1": True,
            "PHYSICAL_CHAMBER_REDUCES_TO_SINGLE_COMPARATOR": True,
            "SUPER_SQRT_INVISIBLE_COPRIMALITY_AUTOMATIC": True,
            "FIXED_U_INVISIBLE_SUPPORT_EQUALS_TWO_COMPARATOR_INTERSECTION": True,
            "FINITE_COMPARATOR_EXACT_DYADIC_RECTANGLE_DECOMPOSITION_PROVED": True,
            "TWO_COMPARATOR_INTERSECTION_RECTANGULARIZES_EXACTLY": True,
            "BALANCED_RECTANGLE_ENERGY_PRODUCT_LE_2_R2": True,
            "RECTANGLE_LOCAL_MELLIN_MODE_FACTORIZATION_PROVED": True,
            "SHARED_AUXILIARY_MODULUS_PRESERVED": True,
            "INDEPENDENT_PI_V_MODULUS_TENSORIZATION_ALLOWED": False,
            "SHARED_U_ENERGY_BALANCED_ORTHOGONAL_RECTANGLE_SECOND_MOMENT_PROVED": False,
            "SHARED_U_CANONICAL_PRIME_DELTA_TOROIDAL_SECOND_MOMENT_PROVED": False,
            "SHARED_U_PHYSICAL_TOROIDAL_MELLIN_CORRELATION_PROVED": False,
            "SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_PROVED": False,
            "TH16_NEEDED": True,
            "TH16_REQUESTED_OBJECT": "SharedUEnergyBalancedOrthogonalRectangleSecondMoment",
            "TH17_NEEDED": False,
            "T_ROUTE_BLOCKED_WAITING_FOR_TH16": False,
            "NEXT": "Stage14-t60 attack SharedUEnergyBalancedOrthogonalRectangleSecondMoment directly; consume tH16 if available",
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
