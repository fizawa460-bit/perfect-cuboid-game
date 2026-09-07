#!/usr/bin/env python3
"""Goal4AJ diagnostic: exact retained140 component locator.

Rebuild the 92 strict-curve linear ideals from the Testa--Stoll cuboids.magma
source lock, recover the 48 singular points intrinsically from pairwise linear
intersections, and identify each exceptional index 93..140 by its exact
incidence signature against the 92 strict curves.  This deliberately avoids
depending on Magma's Points(...) enumeration order.

Diagnostic only: this does not materialize a degree-31 section or F_B.
"""
from __future__ import annotations

from contextlib import redirect_stdout
from fractions import Fraction
from itertools import combinations, product
import hashlib
import io
import json
from pathlib import Path
import runpy
import sys

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
PICARD_DIR = REPO / "stages" / "stage33" / "33-07"
PICARD_SCRIPT = PICARD_DIR / "certify_two_coordinate_swap_picard_rows.py"
SOURCE_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
CURVE_COUNT = 92
POINT_COUNT = 48
KNOWN_COUNT = 140


class K:
    """Q(i,sqrt(2)) in basis 1,i,s,is with exact Fraction coefficients."""

    __slots__ = ("a", "b", "c", "d")

    def __init__(self, a=0, b=0, c=0, d=0):
        self.a = Fraction(a)
        self.b = Fraction(b)
        self.c = Fraction(c)
        self.d = Fraction(d)

    def __add__(self, other):
        o = k(other)
        return K(self.a + o.a, self.b + o.b, self.c + o.c, self.d + o.d)

    __radd__ = __add__

    def __neg__(self):
        return K(-self.a, -self.b, -self.c, -self.d)

    def __sub__(self, other):
        return self + (-k(other))

    def __rsub__(self, other):
        return k(other) - self

    def __mul__(self, other):
        o = k(other)

        def qsmul(x0, x1, y0, y1):
            return x0 * y0 + 2 * x1 * y1, x0 * y1 + x1 * y0

        xu = qsmul(self.a, self.c, o.a, o.c)
        yv = qsmul(self.b, self.d, o.b, o.d)
        xv = qsmul(self.a, self.c, o.b, o.d)
        yu = qsmul(self.b, self.d, o.a, o.c)
        return K(xu[0] - yv[0], xv[0] + yu[0], xu[1] - yv[1], xv[1] + yu[1])

    __rmul__ = __mul__

    def conj_i(self):
        return K(self.a, -self.b, self.c, -self.d)

    def conj_s(self):
        return K(self.a, self.b, -self.c, -self.d)

    def inv(self):
        if not self:
            raise ZeroDivisionError
        ci = self.conj_i()
        cs = self.conj_s()
        num = ci * cs * ci.conj_s()
        den = self * num
        if den.b or den.c or den.d or not den.a:
            raise SystemExit("Q(i,sqrt2) inverse norm regression")
        return K(num.a / den.a, num.b / den.a, num.c / den.a, num.d / den.a)

    def __truediv__(self, other):
        return self * k(other).inv()

    def __eq__(self, other):
        o = k(other)
        return (self.a, self.b, self.c, self.d) == (o.a, o.b, o.c, o.d)

    def __bool__(self):
        return any((self.a, self.b, self.c, self.d))

    def coeffs(self):
        return (self.a, self.b, self.c, self.d)


def k(x):
    return x if isinstance(x, K) else K(x)


Z = K()
O = K(1)
I = K(0, 1)
S = K(0, 0, 1)
IS = I * S
NAMES = ("a1", "a2", "a3", "b1", "b2", "b3", "c")


def row(**kw):
    return [k(kw.get(name, 0)) for name in NAMES]


def build_curves():
    signs = (1, -1)
    out = []

    for e1, e2, e3 in product(signs, repeat=3):
        out.append([row(a1=1), row(a2=1, b3=e1), row(a3=1, b2=e2), row(b1=1, c=e3)])
    for e1, e2, e3 in product(signs, repeat=3):
        out.append([row(a2=1), row(a3=1, b1=e1), row(a1=1, b3=e2), row(b2=1, c=e3)])
    for e1, e2, e3 in product(signs, repeat=3):
        out.append([row(a3=1), row(a1=1, b2=e1), row(a2=1, b1=e2), row(b3=1, c=e3)])
    for e3, e2, e1 in product(signs, repeat=3):
        out.append([row(c=1), row(a1=I, b1=e1), row(a2=I, b2=e2), row(a3=I, b3=e3)])

    for e1, e2 in product(signs, repeat=2):
        out.append([row(b1=1), row(a2=I, a3=e1), row(a1=1, c=e2)])
    for e1, e2 in product(signs, repeat=2):
        out.append([row(b2=1), row(a3=I, a1=e1), row(a2=1, c=e2)])
    for e1, e2 in product(signs, repeat=2):
        out.append([row(b3=1), row(a1=I, a2=e1), row(a3=1, c=e2)])

    for e1, e2, e3 in product(signs, repeat=3):
        out.append([row(a1=1, a2=e1), row(a1=S, b3=e2), row(b1=1, b2=e3)])
    for e1, e2, e3 in product(signs, repeat=3):
        out.append([row(a2=1, a3=e1), row(a2=S, b1=e2), row(b2=1, b3=e3)])
    for e1, e2, e3 in product(signs, repeat=3):
        out.append([row(a3=1, a1=e1), row(a3=S, b2=e2), row(b3=1, b1=e3)])
    for e3, e2, e1 in product(signs, repeat=3):
        out.append([row(a1=I, c=e1), row(b2=I, b3=e2), row(a1=IS, b1=e3)])
    for e3, e2, e1 in product(signs, repeat=3):
        out.append([row(a2=I, c=e1), row(b3=I, b1=e2), row(a2=IS, b2=e3)])
    for e3, e2, e1 in product(signs, repeat=3):
        out.append([row(a3=I, c=e1), row(b1=I, b2=e2), row(a3=IS, b3=e3)])

    if len(out) != CURVE_COUNT:
        raise SystemExit("strict-curve count regression")
    return out


def rref(mat):
    a = [r[:] for r in mat]
    m = len(a)
    n = len(a[0]) if m else 0
    pivots = []
    rr = 0
    for col in range(n):
        pivot = next((i for i in range(rr, m) if a[i][col]), None)
        if pivot is None:
            continue
        a[rr], a[pivot] = a[pivot], a[rr]
        inv = a[rr][col].inv()
        a[rr] = [x * inv for x in a[rr]]
        for i in range(m):
            if i != rr and a[i][col]:
                f = a[i][col]
                a[i] = [a[i][j] - f * a[rr][j] for j in range(n)]
        pivots.append(col)
        rr += 1
        if rr == m:
            break
    return a, pivots


def rank(mat):
    return len(rref(mat)[1])


def unique_projective_nullpoint(mat):
    rr, pivots = rref(mat)
    free = [j for j in range(7) if j not in pivots]
    if len(free) != 1:
        return None
    f = free[0]
    v = [Z for _ in range(7)]
    v[f] = O
    for i, p in enumerate(pivots):
        v[p] = -rr[i][f]
    first = next((x for x in v if x), None)
    if first is None:
        return None
    inv = first.inv()
    return [x * inv for x in v]


def sq(x):
    return x * x


def on_surface(v):
    a1, a2, a3, b1, b2, b3, c = v
    return all(
        not x
        for x in (
            sq(a1) + sq(a2) - sq(b3),
            sq(a2) + sq(a3) - sq(b1),
            sq(a1) + sq(a3) - sq(b2),
            sq(a1) + sq(a2) + sq(a3) - sq(c),
        )
    )


def jacobian(v):
    a1, a2, a3, b1, b2, b3, c = v
    return [
        [2 * a1, 2 * a2, Z, Z, Z, -2 * b3, Z],
        [Z, 2 * a2, 2 * a3, -2 * b1, Z, Z, Z],
        [2 * a1, Z, 2 * a3, Z, -2 * b2, Z, Z],
        [2 * a1, 2 * a2, 2 * a3, Z, Z, Z, -2 * c],
    ]


def is_singular_point(v):
    return on_surface(v) and rank(jacobian(v)) < 4


def point_key(v):
    return tuple(tuple(x.coeffs()) for x in v)


def lin_eval(r, v):
    return sum((a * b for a, b in zip(r, v)), Z)


def curve_contains(curve, v):
    return all(not lin_eval(r, v) for r in curve)


def frac_json(x):
    return [x.numerator, x.denominator]


def k_json(x):
    return [frac_json(z) for z in x.coeffs()]


def point_json(v):
    return [k_json(x) for x in v]


def curve_packet_json(curves):
    return [[[k_json(x) for x in r] for r in curve] for curve in curves]


def csha(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


curves = build_curves()
curve_packet = curve_packet_json(curves)

# Recover singular points without using Magma's Points(...) ordering.
points = {}
for p, q in combinations(range(CURVE_COUNT), 2):
    v = unique_projective_nullpoint(curves[p] + curves[q])
    if v is not None and is_singular_point(v):
        points[point_key(v)] = v
if len(points) != POINT_COUNT:
    raise SystemExit(f"singular-point recovery regression: {len(points)}")

geom_by_sig = {}
for v in points.values():
    sig = tuple(i + 1 for i, curve in enumerate(curves) if curve_contains(curve, v))
    if len(sig) != 10:
        raise SystemExit(f"singular incidence valency regression: {len(sig)}")
    if sig in geom_by_sig:
        raise SystemExit("singular incidence signature collision")
    geom_by_sig[sig] = v
if len(geom_by_sig) != POINT_COUNT:
    raise SystemExit("singular incidence signatures are not unique")

# Reuse the exact retained Picard recovery, but suppress its own bounded report.
sys.path.insert(0, str(PICARD_DIR))
buf = io.StringIO()
with redirect_stdout(buf):
    ns = runpy.run_path(str(PICARD_SCRIPT))
known = ns["known"]
gram = ns["gram"]
pairing = ns["pairing"]
base = ns["base"]
if base.get("upstream_git_blob_sha1") != SOURCE_BLOB:
    raise SystemExit("Testa-Stoll source blob lock moved")
if len(known) != KNOWN_COUNT:
    raise SystemExit("retained known-class count regression")

retained_by_sig = {}
for j in range(POINT_COUNT):
    sig = []
    for i in range(CURVE_COUNT):
        val = pairing(known[i], known[CURVE_COUNT + j], gram)
        if val not in (0, 1):
            raise SystemExit(f"curve-exceptional pairing not incidence at ({i+1},{CURVE_COUNT+j+1}): {val}")
        if val == 1:
            sig.append(i + 1)
    sig = tuple(sig)
    if len(sig) != 10:
        raise SystemExit(f"retained exceptional incidence valency regression at {CURVE_COUNT+j+1}: {len(sig)}")
    if sig in retained_by_sig:
        raise SystemExit("retained exceptional incidence signature collision")
    retained_by_sig[sig] = CURVE_COUNT + j + 1

if set(retained_by_sig) != set(geom_by_sig):
    missing = sorted(set(retained_by_sig) - set(geom_by_sig))
    extra = sorted(set(geom_by_sig) - set(retained_by_sig))
    raise SystemExit(f"geometric/retained incidence signatures mismatch: missing={missing[:2]} extra={extra[:2]}")

node_map = {
    str(retained_by_sig[sig]): {
        "projective_coordinates_basis_1_i_s_is": point_json(geom_by_sig[sig]),
        "incident_strict_curve_indices_1based": list(sig),
    }
    for sig in sorted(retained_by_sig, key=lambda s: retained_by_sig[s])
}

out = {
    "schema": "STAGE35_EX_GOAL4AJ_RETAINED140_COMPONENT_LOCATOR_DIAGNOSTIC_V1",
    "source_locks": {
        "testa_stoll_cuboids_magma_blob_sha1": SOURCE_BLOB,
        "stage33_picard_base_bundle_sha256": base["canonical_sha256"],
    },
    "strict_curve_count": CURVE_COUNT,
    "exceptional_count": POINT_COUNT,
    "known_component_count": KNOWN_COUNT,
    "strict_curve_packet_sha256": csha(curve_packet),
    "all_48_singular_points_recovered_from_strict_curve_pairs": True,
    "all_singular_points_jacobian_rank_deficient": True,
    "each_singular_point_incident_to_exactly_10_strict_curves": True,
    "all_48_geometric_incidence_signatures_unique": True,
    "all_48_retained_exceptional_incidence_signatures_unique": True,
    "geometric_to_retained_exceptional_bijection_exact": True,
    "exceptional_node_locator_93_to_140": node_map,
    "exceptional_node_locator_sha256": csha(node_map),
    "literal_F_B_materialized": False,
    "local_evaluations_computed": False,
    "brauer_manin_obstruction_obtained": False,
    "E1_proved": False,
    "stage35_closed": False,
    "theorem_credit": False,
    "endpoint_credit": False,
}
out["canonical_sha256"] = csha(out)
print("GOAL4AJ_COMPONENT_LOCATOR_JSON=" + json.dumps(out, sort_keys=True, separators=(",", ":")))
print("GOAL4AJ_COMPONENT_LOCATOR=PASS")
