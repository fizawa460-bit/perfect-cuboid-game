#!/usr/bin/env python3
"""Exact local Picard support for the corrected-J2 ct norm splitting.

The generic ct defect of the explicit lift is the split symbol

    {q,g22},  q=t^4-6*t^2+1.

This verifier identifies the eight irreducible components of q=0 on the
resolved Kc model and computes their coordinates in the existing semantic
rank-20 Picard basis.  It uses only exact linear algebra over
Q(i,sqrt(2)); the pinned Stoll intersection data are independently replayed
against the complete semantic Gram/incidence certificate before any new
coordinate is accepted.

This is a support/coordinate certificate.  It deliberately does not infer
the compactified splitting line bundle from the generic norm identity and
does not assign an HS d2 value.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
SEMANTIC = HERE / "j2-semantic-kc-picard-basis.json"
EXPLICIT = HERE / "j2-corrected-explicit-cech-mu2-lift.json"
OUT = HERE / "j2-corrected-ct-norm-picard-support.json"

EXPECTED_SEMANTIC = "c17439c877de3d1cdebd716f4ba2571fb67ec9f07e30d944eafc39ae534380c0"
EXPECTED_EXPLICIT = "6c9333f564637c362b026596833acd26ad2abff27e9c9d75d82ee5c6991cb76b"


def csha(obj):
    return hashlib.sha256(
        json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_locked(path, expected):
    obj = json.loads(path.read_text(encoding="utf-8"))
    body = dict(obj)
    claimed = body.pop("canonical_sha256")
    assert claimed == expected == csha(body), (path, claimed, csha(body))
    return obj


# Q(i,sqrt(2)) in the basis 1,i,sqrt(2),i*sqrt(2).
def k(a=0, b=0, c=0, d=0):
    return tuple(Fraction(x) for x in (a, b, c, d))


ZERO = k()
ONE = k(1)
I = k(0, 1)
S2 = k(0, 0, 1)


def kadd(x, y):
    return tuple(a + b for a, b in zip(x, y))


def kneg(x):
    return tuple(-a for a in x)


def kmul(x, y):
    a, b, c, d = x
    e, f, g, h = y
    return (
        a*e + 2*c*g - b*f - 2*d*h,
        a*f + b*e + 2*(c*h + d*g),
        a*g + c*e - b*h - d*f,
        a*h + b*g + c*f + d*e,
    )


def kinv(x):
    a, b, c, d = x
    cc = (a, -b, c, -d)
    y = kmul(x, cc)
    assert y[1] == y[3] == 0
    u, v = y[0], y[2]
    den = u*u - 2*v*v
    assert den
    return kmul(cc, (u/den, Fraction(0), -v/den, Fraction(0)))


def kdiv(x, y):
    return kmul(x, kinv(y))


def ksum(values):
    out = ZERO
    for value in values:
        out = kadd(out, value)
    return out


def kval(value):
    return value if isinstance(value, tuple) else k(value)


NAMES = ["A1", "A2", "A3", "B1", "B2", "B3"]


def linear(**coeffs):
    return [kval(coeffs.get(name, 0)) for name in NAMES]


def dot(row, point):
    return ksum(kmul(a, b) for a, b in zip(row, point))


def rref(rows, width=6):
    a = [list(row) for row in rows]
    rank = 0
    pivots = []
    for col in range(width):
        pivot = next((j for j in range(rank, len(a)) if a[j][col] != ZERO), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        scale = kinv(a[rank][col])
        a[rank] = [kmul(scale, x) for x in a[rank]]
        for j in range(len(a)):
            if j == rank or a[j][col] == ZERO:
                continue
            scale = a[j][col]
            a[j] = [kadd(x, kneg(kmul(scale, y)))
                    for x, y in zip(a[j], a[rank])]
        pivots.append(col)
        rank += 1
        if rank == len(a):
            break
    return [row for row in a if any(x != ZERO for x in row)], pivots


def nullspace(rows):
    reduced, pivots = rref(rows)
    free = [j for j in range(6) if j not in pivots]
    out = []
    for col in free:
        vec = [ZERO] * 6
        vec[col] = ONE
        for row, pivot in zip(reduced, pivots):
            vec[pivot] = kneg(row[col])
        out.append(vec)
    return out


def quad(point, which):
    A1, A2, A3, B1, B2, B3 = point
    if which == 0:
        return kadd(kadd(kmul(A1, A1), kmul(A2, A2)), kneg(kmul(B3, B3)))
    if which == 1:
        return kadd(kadd(kmul(A2, A2), kmul(A3, A3)), kneg(kmul(B1, B1)))
    return kadd(kadd(kmul(A1, A1), kmul(A3, A3)), kneg(kmul(B2, B2)))


def qbilinear(x, y, which):
    # Polar form, so q(x+y)=q(x)+q(y)+2*B(x,y).
    A1, A2, A3, B1, B2, B3 = range(6)
    if which == 0:
        signs = [(A1, 1), (A2, 1), (B3, -1)]
    elif which == 1:
        signs = [(A2, 1), (A3, 1), (B1, -1)]
    else:
        signs = [(A1, 1), (A3, 1), (B2, -1)]
    return ksum(kmul(k(sign), kmul(x[j], y[j])) for j, sign in signs)


def ptr(point, n):
    return [kadd(a, kmul(k(n), b)) for a, b in zip(point[0], point[1])]


def ptrim(poly):
    poly = list(poly)
    while poly and poly[-1] == ZERO:
        poly.pop()
    return poly


def pdivmod(a, b):
    a, b = ptrim(a), ptrim(b)
    assert b
    q = [ZERO] * max(0, len(a) - len(b) + 1)
    while len(a) >= len(b):
        shift = len(a) - len(b)
        coeff = kdiv(a[-1], b[-1])
        q[shift] = coeff
        for j, value in enumerate(b):
            a[shift+j] = kadd(a[shift+j], kneg(kmul(coeff, value)))
        a = ptrim(a)
    return ptrim(q), a


def pgcd(a, b):
    a, b = ptrim(a), ptrim(b)
    if not a:
        return b
    while b:
        _, rem = pdivmod(a, b)
        a, b = b, rem
    scale = kinv(a[-1])
    return [kmul(scale, x) for x in a]


def common_binary_quad_degree(basis):
    # Replace (x,y) by (X,cX+Y) so the common zero set avoids Y=0.
    assert len(basis) == 2
    for c in range(7):
        leading = [quad(ptr(basis, c), which) for which in range(3)]
        if any(x != ZERO for x in leading):
            break
    else:
        raise AssertionError("all restricted quadrics vanish at every tested infinity point")
    u = ptr(basis, c)
    v = basis[1]
    polys = []
    for which in range(3):
        polys.append([
            quad(v, which),
            kmul(k(2), qbilinear(u, v, which)),
            quad(u, which),
        ])
    g = []
    for poly in polys:
        if ptrim(poly):
            g = poly if not g else pgcd(g, poly)
    return len(ptrim(g)) - 1 if g else 2


def contains(rows, point):
    return all(dot(row, point) == ZERO for row in rows)


def raw_intersection_degree(rows1, rows2):
    basis = nullspace(rows1 + rows2)
    if not basis:
        return 0
    if len(basis) == 1:
        return 1 if all(quad(basis[0], j) == ZERO for j in range(3)) else 0
    if len(basis) == 2:
        return common_binary_quad_degree(basis)
    if len(basis) == 3:
        # Prove that the restricted system contains a smooth conic and another
        # independent conic.  They have no common curve component, so Bezout
        # gives scheme-theoretic degree four in the common projective plane.
        matrices = []
        coeff_rows = []
        for which in range(3):
            matrix = [[qbilinear(basis[a], basis[b], which)
                       for b in range(3)] for a in range(3)]
            matrices.append(matrix)
            coeff_rows.append([
                matrix[0][0], matrix[1][1], matrix[2][2],
                matrix[0][1], matrix[0][2], matrix[1][2],
            ])
        _, pivots = rref(coeff_rows, width=6)
        assert len(pivots) >= 2

        def det3(m):
            return kadd(
                kadd(
                    kmul(m[0][0], kadd(kmul(m[1][1], m[2][2]),
                                        kneg(kmul(m[1][2], m[2][1])))),
                    kneg(kmul(m[0][1], kadd(kmul(m[1][0], m[2][2]),
                                             kneg(kmul(m[1][2], m[2][0]))))),
                ),
                kmul(m[0][2], kadd(kmul(m[1][0], m[2][1]),
                                    kneg(kmul(m[1][1], m[2][0])))),
            )

        smooth = False
        for weights in ((1,0,0),(0,1,0),(0,0,1),(1,1,0),(1,0,1),(0,1,1),(1,1,1)):
            matrix = [[ksum(kmul(k(weights[j]), matrices[j][a][b])
                              for j in range(3))
                       for b in range(3)] for a in range(3)]
            if det3(matrix) != ZERO:
                smooth = True
                break
        assert smooth
        return 4
    raise AssertionError("unexpected positive-dimensional distinct linear-section intersection")


def build_curves():
    curves = []
    labels = []
    for e1 in (1, -1):
        for e2 in (1, -1):
            curves.append([linear(A1=1), linear(A2=1, B3=e1), linear(A3=1, B2=e2)])
            labels.append(("C1a", e1, e2))
    for e1 in (1, -1):
        for e2 in (1, -1):
            curves.append([linear(A2=1), linear(A3=1, B1=e1), linear(A1=1, B3=e2)])
            labels.append(("C1b", e1, e2))
    for e1 in (1, -1):
        for e2 in (1, -1):
            curves.append([linear(A3=1), linear(A1=1, B2=e1), linear(A2=1, B1=e2)])
            labels.append(("C1c", e1, e2))
    for e3 in (1, -1):
        for e2 in (1, -1):
            for e1 in (1, -1):
                curves.append([linear(A1=I, B1=e1), linear(A2=I, B2=e2), linear(A3=I, B3=e3)])
                labels.append(("C1d", e1, e2, e3))
    for e1 in (1, -1):
        curves.append([linear(B1=1), linear(A2=I, A3=e1)])
        labels.append(("C2a", e1))
    for e1 in (1, -1):
        curves.append([linear(B2=1), linear(A3=I, A1=e1)])
        labels.append(("C2b", e1))
    for e1 in (1, -1):
        curves.append([linear(B3=1), linear(A1=I, A2=e1)])
        labels.append(("C2c", e1))
    for e1 in (1, -1):
        for e2 in (1, -1):
            for e3 in (1, -1):
                curves.append([linear(A1=1, A2=e1), linear(A1=S2, B3=e2), linear(B1=1, B2=e3)])
                labels.append(("C3a", e1, e2, e3))
    for e1 in (1, -1):
        for e2 in (1, -1):
            for e3 in (1, -1):
                curves.append([linear(A2=1, A3=e1), linear(A2=S2, B1=e2), linear(B2=1, B3=e3)])
                labels.append(("C3b", e1, e2, e3))
    for e1 in (1, -1):
        for e2 in (1, -1):
            for e3 in (1, -1):
                curves.append([linear(A3=1, A1=e1), linear(A3=S2, B2=e2), linear(B3=1, B1=e3)])
                labels.append(("C3c", e1, e2, e3))
    iroot2 = kmul(I, S2)
    for e3 in (1, -1):
        for e2 in (1, -1):
            curves.append([linear(B2=I, B3=e2), linear(A1=iroot2, B1=e3)])
            labels.append(("C3d", e2, e3))
    for e3 in (1, -1):
        for e2 in (1, -1):
            curves.append([linear(B3=I, B1=e2), linear(A2=iroot2, B2=e3)])
            labels.append(("C3e", e2, e3))
    for e3 in (1, -1):
        for e2 in (1, -1):
            curves.append([linear(B1=I, B2=e2), linear(A3=iroot2, B3=e3)])
            labels.append(("C3f", e2, e3))
    assert len(curves) == 62
    return curves, labels


def gram20(semantic):
    g17 = semantic["gram17"]
    incidence = semantic["incidence17x12"]
    triple = semantic["semantic_exceptional_indices_0based"]
    out = [row[:] + [incidence[i][j] for j in triple]
           for i, row in enumerate(g17)]
    for a, j in enumerate(triple):
        row = [incidence[i][j] for i in range(17)] + [0, 0, 0]
        row[17+a] = -2
        out.append(row)
    return out


def solve_row_coordinates(gram, pairings):
    # Solve x*gram=pairings over Q by Gauss-Jordan elimination.
    n = len(gram)
    aug = [[Fraction(gram[j][i]) for j in range(n)] + [Fraction(pairings[i])]
           for i in range(n)]
    for col in range(n):
        pivot = next(j for j in range(col, n) if aug[j][col])
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [x/scale for x in aug[col]]
        for j in range(n):
            if j == col or not aug[j][col]:
                continue
            scale = aug[j][col]
            aug[j] = [x-scale*y for x, y in zip(aug[j], aug[col])]
    answer = [aug[i][-1] for i in range(n)]
    assert all(x.denominator == 1 for x in answer)
    return [int(x) for x in answer]


semantic = load_locked(SEMANTIC, EXPECTED_SEMANTIC)
explicit = load_locked(EXPLICIT, EXPECTED_EXPLICIT)
assert explicit["galois_defect_generic_splittings"]["ct"]["formula"] == (
    "ct(lambda_D)-lambda_D={ct(f2)/f2,g22}={q,g22}"
)

curves, labels = build_curves()
slots = semantic["curve_slots_1based"]
points = [[kval(int(x)) for x in rec["coords"]]
          for rec in semantic["semantic_point_order"]]

# Full independent replay of the retained semantic intersection input.
incidence = [[int(contains(curves[j-1], point)) for point in points] for j in slots]
assert incidence == semantic["incidence17x12"]
replayed = []
for j in slots:
    row = []
    for h in slots:
        if j == h:
            row.append(0 if 21 <= j <= 26 or 51 <= j <= 62 else -2)
        else:
            try:
                raw = raw_intersection_degree(curves[j-1], curves[h-1])
            except AssertionError as exc:
                raise AssertionError((j, h, labels[j-1], labels[h-1], exc)) from exc
            common_nodes = sum(contains(curves[j-1], p) and contains(curves[h-1], p)
                               for p in points)
            row.append(raw-common_nodes)
    replayed.append(row)
assert replayed == semantic["gram17"]

g20 = gram20(semantic)
target_rows = []
for j in range(27, 35):
    pairings = []
    for h in slots:
        try:
            raw = raw_intersection_degree(curves[j-1], curves[h-1])
        except AssertionError as exc:
            raise AssertionError((j, h, labels[j-1], labels[h-1], exc)) from exc
        common_nodes = sum(contains(curves[j-1], p) and contains(curves[h-1], p)
                           for p in points)
        pairings.append(raw-common_nodes)
    pairings += [int(contains(curves[j-1], points[a]))
                 for a in semantic["semantic_exceptional_indices_0based"]]
    coords = solve_row_coordinates(g20, pairings)
    family, e1, e2, e3 = labels[j-1]
    assert family == "C3a"
    root, root_value = {
        (1, 1): ("r1=1+sqrt(2)", k(1, 0, 1)),
        (1, -1): ("r4=1-sqrt(2)", k(1, 0, -1)),
        (-1, 1): ("r2=-1-sqrt(2)", k(-1, 0, -1)),
        (-1, -1): ("r3=-1+sqrt(2)", k(-1, 0, 1)),
    }[(e1, e2)]
    root2 = kmul(root_value, root_value)
    root4 = kmul(root2, root2)
    assert kadd(kadd(root4, kneg(kmul(k(6), root2))), ONE) == ZERO
    # On the Stoll chart t=A2/(A1+B3), the curve equations imply
    # A2-root_value*(A1+B3)=0.  This proves that CsK[j] is a component
    # of the stated q-root fiber rather than merely matching its signs.
    chart_row = linear(A1=kneg(root_value), A2=1, B3=kneg(root_value))
    assert len(rref(curves[j-1])[0]) == len(rref(curves[j-1] + [chart_row])[0])
    target_rows.append({
        "CsK_index_1based": j,
        "signs_e1_e2_e3": [e1, e2, e3],
        "q_root": root,
        "equations": [
            f"A1{('+' if e1 == 1 else '-') }A2=0",
            f"sqrt(2)*A1{('+' if e2 == 1 else '-') }B3=0",
            f"B1{('+' if e3 == 1 else '-') }B2=0",
        ],
        "intersection_signature_against_semantic_basis": pairings,
        "marked_semantic_PicK_coordinates": coords,
    })

# Each q-root fiber is the union of its two e3 components.  The four fiber
# sums must have one common Picard class.
fiber_sums = []
for a in range(0, 8, 2):
    fiber_sums.append([x+y for x, y in zip(
        target_rows[a]["marked_semantic_PicK_coordinates"],
        target_rows[a+1]["marked_semantic_PicK_coordinates"],
    )])
assert all(row == fiber_sums[0] for row in fiber_sums)

# sqrt(2)-conjugation flips e2 and fixes e1,e3; complex conjugation fixes
# every coefficient of these eight curves.  Derive the permutation from the
# reconstructed Stoll labels rather than accepting a manually entered table.
index_by_sign = {labels[j-1][1:]: j for j in range(27, 35)}
ct_component_permutation = [
    [index_by_sign[(e1, 1, e3)], index_by_sign[(e1, -1, e3)]]
    for e1 in (1, -1) for e3 in (1, -1)
]
assert ct_component_permutation == [[27,29],[28,30],[31,33],[32,34]]
assert all(coeff[1] == coeff[3] == 0
           for j in range(27, 35) for row in curves[j-1] for coeff in row)

cert = {
    "schema": "STAGE33_05_J2_CORRECTED_CT_NORM_PICARD_SUPPORT_V1",
    "status": "PASS_EXACT_CT_NORM_Q_FIBER_COMPONENTS_AND_MARKED_PICARD_COORDINATES_SPLITTING_LINE_BUNDLE_OPEN",
    "source_locks": {
        "semantic_picard_basis": {
            "path": "stages/stage33/33-12/j2-semantic-kc-picard-basis.json",
            "canonical_sha256": EXPECTED_SEMANTIC,
        },
        "explicit_surface_mu2_lift": {
            "path": "stages/stage33/33-12/j2-corrected-explicit-cech-mu2-lift.json",
            "canonical_sha256": EXPECTED_EXPLICIT,
        },
        "pinned_stoll_source": {
            "repository": "MichaelStollBayreuth/Verification",
            "commit": "51233ed5ef2bf228fac9416c66db9adc0ebcaadd",
            "path": "Cuboids/cuboids.magma",
            "git_blob_sha1": "0422b69847f2afb97cb7b3ed02ebef91279f61b1",
        },
    },
    "exact_replay": {
        "field": "Q(i,sqrt(2))",
        "all_62_stoll_linear_section_equations_rebuilt": True,
        "semantic_incidence_17x12_replayed": True,
        "semantic_gram17_replayed": True,
        "semantic_gram20_determinant": semantic["semantic_gram20_determinant"],
        "remote_CAS_required": False,
    },
    "ct_norm_support": {
        "q": "t^4-6*t^2+1",
        "q_zero_fiber_components": target_rows,
        "component_count": 8,
        "components_per_root": 2,
        "common_q_fiber_class_marked_semantic_PicK_coordinates": fiber_sums[0],
        "ct_component_permutation_1based": ct_component_permutation,
        "cc_fixes_each_component": True,
        "q_fiber_component_coordinates_materialized": True,
        "norm_splitting_cartier_divisor_on_quotient_materialized": False,
        "norm_splitting_determinant_line_bundle_on_quotient_materialized": False,
    },
    "exact_information_boundary": {
        "cc_defect_marked_Pic_mod2_coordinates_materialized": False,
        "ct_defect_support_components_materialized": True,
        "ct_defect_marked_Pic_mod2_coordinates_materialized": False,
        "integral_Pic_lift_materialized": False,
        "HS_d2_2cocycle_materialized": False,
        "HS_d2_zero_or_nonzero_proved": False,
        "reason": "The eight q-fiber components and all marked Picard coordinates are exact. Generic triviality of {q,g22} does not determine its compactified Pic/2 extension. The remaining load-bearing step is to derive the Cartier divisor or determinant line bundle of the explicit norm nullhomotopy on the resolved quotient, then pull that class back to the marked Kc lattice.",
    },
    "next_exact_leaf": "DERIVE_CT_NORM_SPLITTING_DETERMINANT_LINE_BUNDLE_ON_RESOLVED_QUOTIENT_THEN_PULL_BACK_TO_MARKED_PIC_KC_MOD2_AND_COMPUTE_INTEGRAL_BOCKSTEIN",
    "promotion_firewall": {
        "old_j2_arithmetic_descent_reused": False,
        "old_ell_Q_reused": False,
        "historical_kummer_glue_reused": False,
        "Q_defined_descent_credit_restored": False,
        "R5_full_repair_exit_reached": False,
        "stage33_05_reclosed": False,
        "stage33_12_closed_exact": False,
        "stage33_13_released": False,
        "stage33_progress": "5/11",
        "theorem_credit": False,
        "receiver_credit": False,
        "endpoint_credit": False,
        "perfect_cuboid_existence_claim": False,
        "perfect_cuboid_nonexistence_claim": False,
    },
}
cert["canonical_sha256"] = csha(cert)
OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps({
    "success": True,
    "status": cert["status"],
    "component_count": 8,
    "q_fiber_component_coordinates_materialized": True,
    "ct_defect_marked_Pic_mod2_coordinates_materialized": False,
    "canonical_sha256": cert["canonical_sha256"],
    "next_exact_leaf": cert["next_exact_leaf"],
}, indent=2, sort_keys=True))
