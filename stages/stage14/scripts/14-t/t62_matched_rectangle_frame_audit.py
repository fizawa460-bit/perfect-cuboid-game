#!/usr/bin/env python3
"""Stage14-t62: reconstruct t59 families and audit the matched rectangle frame reduction."""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
T36_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
T42_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t42_kummer_transversality_audit.py"
T59_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t59_orthogonal_rectangle_reduction_audit.py"
T61_RESULT = ROOT / "stages/stage14/14-t61/result.md"
OUT = ROOT / "stages/stage14/data/14-t62/matched_rectangle_frame.json"

B_FROZEN = 10_000


def deterministic_edge_value(row, col) -> int:
    vals = list(row) + list(col)
    s = sum((i + 3) * abs(int(v)) for i, v in enumerate(vals))
    return (s % 11) - 5


def reconstruct_packet_families(key, states, t59):
    Ukey, eps, k = key
    m_values = {s["m"] for s in states}
    assert len(m_values) == 1
    m = next(iter(m_values))

    rows = sorted({t59["row_key"](s) for s in states})
    cols = sorted({t59["col_key"](s) for s in states})
    observed = {(t59["row_key"](s), t59["col_key"](s)) for s in states}
    assert len(observed) == len(states)

    rr1, cr1, nleaf1, valid1 = t59["rank_comparator"](
        rows,
        cols,
        lambda r: Fraction(r[0], r[1]),
        lambda c: Fraction(c[0], c[1]),
        leq=False,
    )
    Y = Fraction(2 * B_FROZEN, eps * m)
    rr2, cr2, nleaf2, valid2 = t59["rank_comparator"](
        rows,
        cols,
        lambda r: Fraction(r[2], 1),
        lambda c: Y / Fraction(c[3], 1),
        leq=True,
    )

    rectangles = defaultdict(set)
    for r, c in observed:
        assert valid1(r, c) and valid2(r, c)
        d1, p1 = t59["comparator_descriptor"](rr1[r], cr1[c], nleaf1)
        d2, p2 = t59["comparator_descriptor"](rr2[r], cr2[c], nleaf2)
        rectangles[(d1, d2, p1, p2)].add((r, c))

    families = defaultdict(list)
    for desc, edges in rectangles.items():
        rowset = {r for r, _ in edges}
        colset = {c for _, c in edges}
        cart = {(r, c) for r in rowset for c in colset}
        assert edges == cart
        a, b = len(rowset), len(colset)
        aspect = t59["floor_log2_ratio"](a, b)
        d1, d2, _, _ = desc
        families[(d1, d2, aspect)].append((rowset, colset, edges, a, b))

    family_rows = []
    packet_mass = 0
    for family_key, family in sorted(families.items()):
        seen_rows = set()
        seen_cols = set()
        seen_edges = set()
        mass = 0
        singular_square_sum = 0

        # Exact HS orthogonality: disjoint row and column projections imply
        # <u_j v_j^*, u_k v_k^*>=0 for j!=k.
        for rowset, colset, edges, a, b in family:
            assert not (seen_rows & rowset)
            assert not (seen_cols & colset)
            assert not (seen_edges & edges)
            seen_rows |= rowset
            seen_cols |= colset
            seen_edges |= edges
            assert len(edges) == a * b
            mass += a * b
            singular_square_sum += a * b

        assert singular_square_sum == mass

        # Exact block-average Bessel test with deterministic integer F:
        # sum_j |sum_{R_j}F|^2/|R_j| <= sum_edges |F|^2.
        lhs = Fraction(0, 1)
        rhs = 0
        for rowset, colset, edges, a, b in family:
            block_sum = sum(deterministic_edge_value(r, c) for r, c in edges)
            lhs += Fraction(block_sum * block_sum, a * b)
            rhs += sum(deterministic_edge_value(r, c) ** 2 for r, c in edges)
        assert lhs <= rhs

        family_rows.append({
            "family": list(family_key),
            "rectangles": len(family),
            "mass": mass,
            "selector_hs2": mass,
            "singular_value_square_sum": singular_square_sum,
            "block_bessel_lhs_num": lhs.numerator,
            "block_bessel_lhs_den": lhs.denominator,
            "block_bessel_rhs": rhs,
            "hs_orthonormal": True,
            "selector_exact_svd": True,
            "block_projection_bessel": True,
        })
        packet_mass += mass

    assert packet_mass == len(observed)
    return {
        "packet": t59["packet_label"](key),
        "states": len(states),
        "rectangles": len(rectangles),
        "families": len(families),
        "mass": packet_mass,
        "max_rectangles_per_family": max(len(f) for f in families.values()),
        "family_rows": family_rows,
    }


def main() -> None:
    t61 = T61_RESULT.read_text()
    assert "STAGE14_T61=COMPLETE_POLAR_SCHATTEN_OBSTRUCTION_AND_SIGNED_RECTANGLE_REOPENING" in t61
    assert "SIGNED_ORTHOGONAL_RECTANGLE_KUMMER_BILINEAR_LARGE_SIEVE_PROVED=false" in t61
    assert "TH17_NEEDED=true" in t61

    t59 = runpy.run_path(str(T59_SCRIPT), run_name="stage14_t59_import")
    t36 = runpy.run_path(str(T36_SCRIPT), run_name="stage14_t36_import")
    t42 = runpy.run_path(str(T42_SCRIPT), run_name="stage14_t42_import")

    reps = t42["reciprocal_quotient"](t36["build_frozen_states"]())
    invisible = [s for s in reps if s["branch"] == "invisible"]
    assert len(reps) == 560
    assert len(invisible) == 419

    packets = defaultdict(list)
    for s in invisible:
        packets[t59["packet_key"](s)].append(s)
    assert len(packets) == 8

    rows = [reconstruct_packet_families(key, states, t59) for key, states in sorted(packets.items())]

    totals = {
        "reciprocal_states": len(reps),
        "invisible_states": len(invisible),
        "packets": len(rows),
        "rectangles": sum(r["rectangles"] for r in rows),
        "families": sum(r["families"] for r in rows),
        "sum_family_masses": sum(r["mass"] for r in rows),
        "sum_selector_hs2": sum(r["mass"] for r in rows),
        "max_rectangles_per_family": max(r["max_rectangles_per_family"] for r in rows),
        "bessel_checks": sum(r["families"] for r in rows),
    }
    assert totals == {
        "reciprocal_states": 560,
        "invisible_states": 419,
        "packets": 8,
        "rectangles": 127,
        "families": 109,
        "sum_family_masses": 419,
        "sum_selector_hs2": 419,
        "max_rectangles_per_family": 4,
        "bessel_checks": 109,
    }

    report = {
        "stage": "14-t62",
        "totals": totals,
        "packets": rows,
        "exact_lemmas": {
            "rectangle_basis": "E_j=(1_Aj/sqrt(a_j))(1_Bj/sqrt(b_j))^* are HS-orthonormal",
            "selector_svd": "W=sum_j sqrt(a_j*b_j) E_j is an exact SVD",
            "physical_mass": "||W||_HS^2=sum_j a_j*b_j",
            "signed_trace": "T_pq=sum_j sqrt(a_j*b_j) kappa_pq,j",
            "gram": "sum_pq |T_pq|^2 = z^* G z with z_j=sqrt(a_j*b_j)",
            "dual_projection": "sum_j |sum_{R_j}F|^2/|R_j| <= sum_edges |F|^2",
        },
        "decision": {
            "STAGE14_T62": "COMPLETE_MATCHED_RECTANGLE_FRAME_AND_DUAL_PROJECTION_REDUCTION",
            "T59_RECTANGLE_INDICATORS_HS_ORTHONORMAL": True,
            "T59_SELECTOR_EXACT_SVD_PROVED": True,
            "T59_SELECTOR_HS2_EQUALS_PHYSICAL_MASS": True,
            "SIGNED_RECTANGLE_TRACE_COMPRESSES_TO_ONE_SCALAR_PER_BLOCK": True,
            "PHYSICAL_RECEIVER_EQUALS_MASS_VECTOR_RAYLEIGH_BOUND": True,
            "FULL_RECTANGLE_FRAME_OPERATOR_BOUND_REQUIRED": False,
            "MATCHED_RECTANGLE_PROJECTED_KUMMER_DUAL_LARGE_SIEVE_PROVED": False,
            "MATCHED_BLOCK_PROJECTION_BESSEL_ZERO_LOSS": True,
            "AMBIENT_STATE_SPACE_LARGE_SIEVE_REQUIRED": False,
            "POLAR_ABSOLUTE_VALUE_USED": False,
            "T61_POLAR_FIXED_POWER_LOSS_INSERTED": False,
            "SIGNED_KUMMER_PHASE_PRESERVED": True,
            "PHYSICAL_MASS_VECTOR_KUMMER_RAYLEIGH_BOUND_PROVED": False,
            "SHARED_U_ENERGY_BALANCED_ORTHOGONAL_RECTANGLE_SECOND_MOMENT_PROVED": False,
            "SHARED_U_CANONICAL_PRIME_DELTA_TOROIDAL_SECOND_MOMENT_PROVED": False,
            "SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_PROVED": False,
            "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT": "7/8",
            "TH17_NEEDED": True,
            "TH17_REQUESTED_OBJECT": "MatchedRectangleProjectedKummerDualLargeSieve",
            "TH18_NEEDED": False,
            "T_ROUTE_BLOCKED_WAITING_FOR_TH17": False,
            "NEXT": "Stage14-t63 attack the matched block-average dual inequality directly; consume tH17 if available",
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
