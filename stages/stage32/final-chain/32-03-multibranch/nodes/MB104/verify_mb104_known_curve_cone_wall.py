#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
NODE = ROOT / "stages/stage32/final-chain/32-03-multibranch/nodes/MB104"
WALL = NODE / "KNOWN-CURVE-CONE-WALL.json"

STAGE29 = ROOT / "stages/stage29/29-02c-LG2/result.md"
STAGE29_BLOB = "820ed4e1b1a53db14085678de6f186b59ae0ea48"
UPSTREAM_COMMIT = "51233ed5ef2bf228fac9416c66db9adc0ebcaadd"
UPSTREAM_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


# Gaussian integer pair a+b*i.
def ga(x, y): return (x[0] + y[0], x[1] + y[1])
def gn(x): return (-x[0], -x[1])
def gm(x, y): return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])
def gs(n, x): return (n * x[0], n * x[1])
G0, G1, GM1, GI, GMI = (0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)
GUNITS = (G0, G1, GM1, GI, GMI)


def ginv_unit(x):
    assert x in (G1, GM1, GI, GMI)
    return (x[0], -x[1])


def pcanon(p):
    for x in p:
        if x != G0:
            inv = ginv_unit(x)
            return tuple(gm(inv, y) for y in p)
    raise AssertionError("zero projective point")


def surface_ok(p):
    a1, a2, a3, b1, b2, b3, c = p
    sq = lambda x: gm(x, x)
    vals = [
        ga(ga(sq(a1), sq(a2)), gn(sq(b3))),
        ga(ga(sq(a2), sq(a3)), gn(sq(b1))),
        ga(ga(sq(a1), sq(a3)), gn(sq(b2))),
        ga(ga(ga(sq(a1), sq(a2)), sq(a3)), gn(sq(c))),
    ]
    return all(v == G0 for v in vals)


# Q(i,sqrt(2)) represented as z0+z1*s with Gaussian z0,z1.
def fa(x, y): return (ga(x[0], y[0]), ga(x[1], y[1]))
def fn(x): return (gn(x[0]), gn(x[1]))
def fm(x, y):
    z0, z1 = x
    w0, w1 = y
    return (ga(gm(z0, w0), gs(2, gm(z1, w1))), ga(gm(z0, w1), gm(z1, w0)))

F0 = (G0, G0)
FI = (GI, G0)
FS = (G0, G1)


def emb(x): return (x, G0)
def mul_i(x): return fm(FI, x)
def mul_s(x): return fm(FS, x)
def signed_add(x, sign, y): return fa(x, y if sign == 1 else fn(y))
def all_zero(vals): return all(v == F0 for v in vals)


def c1_vals(group, e1, e2, e3, p):
    a1, a2, a3, b1, b2, b3, c = map(emb, p)
    if group == 0:
        return [a1, signed_add(a2,e1,b3), signed_add(a3,e2,b2), signed_add(b1,e3,c)]
    if group == 1:
        return [a2, signed_add(a3,e1,b1), signed_add(a1,e2,b3), signed_add(b2,e3,c)]
    if group == 2:
        return [a3, signed_add(a1,e1,b2), signed_add(a2,e2,b1), signed_add(b3,e3,c)]
    return [c, signed_add(mul_i(a1),e1,b1), signed_add(mul_i(a2),e2,b2), signed_add(mul_i(a3),e3,b3)]


def c2_vals(group, e1, e2, p):
    a1, a2, a3, b1, b2, b3, c = map(emb, p)
    if group == 0:
        return [b1, signed_add(mul_i(a2),e1,a3), signed_add(a1,e2,c)]
    if group == 1:
        return [b2, signed_add(mul_i(a3),e1,a1), signed_add(a2,e2,c)]
    return [b3, signed_add(mul_i(a1),e1,a2), signed_add(a3,e2,c)]


def c3_vals(group, e1, e2, e3, p):
    a1, a2, a3, b1, b2, b3, c = map(emb, p)
    if group == 0:
        return [signed_add(a1,e1,a2), signed_add(mul_s(a1),e2,b3), signed_add(b1,e3,b2)]
    if group == 1:
        return [signed_add(a2,e1,a3), signed_add(mul_s(a2),e2,b1), signed_add(b2,e3,b3)]
    if group == 2:
        return [signed_add(a3,e1,a1), signed_add(mul_s(a3),e2,b2), signed_add(b3,e3,b1)]
    if group == 3:
        return [signed_add(mul_i(a1),e1,c), signed_add(mul_i(b2),e2,b3), signed_add(mul_i(mul_s(a1)),e3,b1)]
    if group == 4:
        return [signed_add(mul_i(a2),e1,c), signed_add(mul_i(b3),e2,b1), signed_add(mul_i(mul_s(a2)),e3,b2)]
    return [signed_add(mul_i(a3),e1,c), signed_add(mul_i(b1),e2,b2), signed_add(mul_i(mul_s(a3)),e3,b3)]


def reconstruct_points():
    # A singular point has the three coordinates of one of the six rank-3
    # quadrics equal to zero. The source-locked equations then give 8 points
    # for each triple, for 48 total. All normalized coordinates are Gaussian units.
    triples = [(0,3,6),(1,4,6),(2,5,6),(0,1,5),(0,2,4),(1,2,3)]
    pts = set()
    for tri in triples:
        rem = [j for j in range(7) if j not in tri]
        for vals in product(GUNITS, repeat=4):
            if all(v == G0 for v in vals):
                continue
            p = [G0] * 7
            for j, v in zip(rem, vals):
                p[j] = v
            if surface_ok(p):
                pts.add(pcanon(p))
    assert len(pts) == 48
    return sorted(pts)


def incidence(pts, family):
    rows = []
    if family == 1:
        for group in range(4):
            for e1,e2,e3 in product((1,-1), repeat=3):
                rows.append([j for j,p in enumerate(pts) if all_zero(c1_vals(group,e1,e2,e3,p))])
    elif family == 2:
        for group in range(3):
            for e1,e2 in product((1,-1), repeat=2):
                rows.append([j for j,p in enumerate(pts) if all_zero(c2_vals(group,e1,e2,p))])
    else:
        for group in range(6):
            for e1,e2,e3 in product((1,-1), repeat=3):
                rows.append([j for j,p in enumerate(pts) if all_zero(c3_vals(group,e1,e2,e3,p))])
    return rows


def degree_incidence_ray_intersection(k, degree, nodes):
    # D_k=6kH-kE_total and a known strict transform C has H.C=degree,
    # E_total.C=nodes because every listed node contributes one.
    return 6 * k * degree - k * nodes


def main():
    assert git_blob_sha(STAGE29) == STAGE29_BLOB
    stage29 = STAGE29.read_text()
    assert "H^2 = K_S^2 = 16" in stage29

    wall = json.loads(WALL.read_text())
    assert wall["source_locks"]["upstream_commit"] == UPSTREAM_COMMIT
    assert wall["source_locks"]["upstream_blob_sha1"] == UPSTREAM_BLOB

    pts = reconstruct_points()
    fam1, fam2, fam3 = incidence(pts,1), incidence(pts,2), incidence(pts,3)
    assert len(fam1) == 32 and {len(r) for r in fam1} == {6}
    assert len(fam2) == 12 and {len(r) for r in fam2} == {8}
    assert len(fam3) == 48 and {len(r) for r in fam3} == {4}

    for rows, per_node in ((fam1,4),(fam2,2),(fam3,4)):
        counts = [0] * 48
        for row in rows:
            for j in row:
                counts[j] += 1
        assert set(counts) == {per_node}

    inc = wall["exact_incidence_reconstruction"]
    assert inc["G1_conics"] == {"count":32,"degree":2,"nodes_per_curve":6,"curves_per_node":4}
    assert inc["G2_boundary_elliptics"] == {"count":12,"degree":4,"nodes_per_curve":8,"curves_per_node":2}
    assert inc["G3_other_elliptics"] == {"count":48,"degree":4,"nodes_per_curve":4,"curves_per_node":4}

    for k in range(1, 101):
        d = 96 * k
        M = 48 * (2 * k)
        D2 = 480 * k * k
        assert M == d
        assert degree_incidence_ray_intersection(k,2,6) == 6*k
        assert degree_incidence_ray_intersection(k,4,8) == 16*k
        assert degree_incidence_ray_intersection(k,4,4) == 20*k
        assert 2*k > 0
        # Existing MB104 Hodge mass bound, genus one.
        sum_M2 = 48 * (2*k)**2
        assert sum_M2 <= d*d//8 + 2*d
        # Riemann--Roch effectivity calculation.
        chi = 8 + (D2 - d)//2
        assert chi == 240*k*k - 48*k + 8
        assert chi > 0
        assert 16 - d < 0
        # A hypothetical integral genus-one member needs this much delta.
        delta = (D2 + d)//2
        assert delta == 240*k*k + 48*k

    assert wall["symmetric_scaling_ray"]["strictly_positive_on_all_140_known_curves"] is True
    assert wall["riemann_roch_effectivity"]["effective_divisor_class_for_every_k_ge_1"] is True
    assert wall["riemann_roch_effectivity"]["integral_member_claimed"] is False
    assert wall["riemann_roch_effectivity"]["low_geometric_genus_member_claimed"] is False
    assert wall["decision"]["finite_degree_window_proved"] is False
    assert wall["firewalls"]["receiver_credit"] is False
    assert wall["firewalls"]["merge_authorized"] is False

    print("MB104 known-curve cone wall verifier PASS")
    print("48 nodes; G1/G2/G3 incidences = (32x6),(12x8),(48x4)")
    print("D_k=6kH-kE is effective as a divisor class and positive on all 140 known curves")
    print("finite degree window remains OPEN: low-genus integral-member control is still missing")


if __name__ == "__main__":
    main()
