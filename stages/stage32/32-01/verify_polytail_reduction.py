#!/usr/bin/env python3
"""Exact Stage32-01 polytail reduction certificate.

Consumes picard-core.json produced from the pinned upstream Magma source.
No floating point or polyhedral package is used.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CORE = ROOT / "picard-core.json"
OUT = ROOT / "polytail-reduction-certificate.json"


def bareiss_det(a):
    a = [list(map(int, row)) for row in a]
    n = len(a)
    sign = 1
    prev = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            swap = next((r for r in range(k + 1, n) if a[r][k] != 0), None)
            if swap is None:
                return 0
            a[k], a[swap] = a[swap], a[k]
            sign = -sign
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * pivot - a[i][k] * a[k][j]) // prev
        prev = pivot
        for i in range(k + 1, n):
            a[i][k] = 0
        for j in range(k + 1, n):
            a[k][j] = 0
    return sign * a[n - 1][n - 1]


def row_vec_mul(v, m):
    return [sum(int(v[i]) * int(m[i][j]) for i in range(len(v))) for j in range(len(m[0]))]


def main():
    core = json.loads(CORE.read_text())
    assert core["schema"] == "STAGE32_PICARD_CORE_INDLIST_V1"
    assert core["rank"] == 64
    assert core["known_curve_count"] == 92
    assert core["node_count"] == 48
    assert core["known_class_count"] == 140
    assert core["h2"] == 16

    G = core["basis_gram"]
    A = core["raw_cross_pairings_with_basis"]
    H = core["hyperplane"]
    basis_indices = core["basis_known_indices_1based"]
    assert len(G) == 64 and all(len(r) == 64 for r in G)
    assert len(A) == 140 and all(len(r) == 64 for r in A)
    assert len(H) == 64
    assert len(basis_indices) == 64

    # The 64 chosen known classes are a primitive Picard basis upstream.
    # Their intersection rows must therefore be exactly the exported Gram matrix.
    assert all(A[idx - 1] == G[j] for j, idx in enumerate(basis_indices))
    det = bareiss_det(G)
    assert det == int(core["basis_gram_determinant"]) == -268435456

    hform = row_vec_mul(H, G)
    h2 = sum(int(H[j]) * hform[j] for j in range(64))
    assert h2 == 16

    # Exact positive dual-cone certificate discovered after the audited preflight:
    #
    #   19 (H . x) = sum_{92 known nonexceptional curves D} (D . x)
    #                + 5 sum_{48 exceptional curves E} (E . x).
    #
    # This is checked coordinatewise in the Picard basis, using integers only.
    weighted = [0] * 64
    for i, row in enumerate(A):
        w = 1 if i < 92 else 5
        for j, value in enumerate(row):
            weighted[j] += w * int(value)
    target = [19 * int(x) for x in hform]
    assert weighted == target

    # Since all 140 intersections are constrained >=0 for a genuinely new
    # irreducible class, H.x=0 forces every one of them to vanish.  The 64
    # basis rows have nonzero determinant, hence x=0.  Therefore the homogeneous
    # tail cone has no nonzero H-degree-zero ray, and every fixed positive-degree
    # slice is bounded/compact.  Moreover the identity gives immediate per-row
    # bounds used by the graded branch-and-bound enumerator.
    cert = {
        "schema": "STAGE32_32_01_POLYTAIL_REDUCTION_V1",
        "source_core_schema": core["schema"],
        "source_core_sha256": core["canonical_sha256_without_this_field"],
        "basis_gram_determinant": det,
        "basis_rows_full_rank": True,
        "known_curve_count": 92,
        "exceptional_curve_count": 48,
        "positive_identity": {
            "equation": "19*(H.x)=sum_curve(D.x)+5*sum_exceptional(E.x)",
            "curve_weight": 1,
            "exceptional_weight": 5,
            "coordinatewise_exact": True,
        },
        "homogeneous_tail_H0_is_zero": True,
        "fixed_positive_degree_slices_bounded": True,
        "intersection_bounds_for_degree_d": {
            "known_curve": "0 <= D.x <= 19*d",
            "exceptional_curve": "0 <= E.x <= floor(19*d/5)",
        },
        "raw_63d_cvp_required_for_tail_certification": False,
        "normaliz_tail_cone_required": False,
        "full_d176_d192_numerical_orbit_census": False,
        "r29_lg2_numerical_component_complete": False,
    }
    OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
    print(json.dumps(cert, sort_keys=True))


if __name__ == "__main__":
    main()
