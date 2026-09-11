#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
from collections import deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
NODE = ROOT / "stages/stage32/final-chain/32-03-multibranch/nodes/MB104"

LOCKS = {
    "stages/stage32/final-chain/32-03-multibranch/nodes/MB103/CERTIFICATE.json": "6d2b7acb667e7757a4f859b7eb0680ce4fd3aae0",
    "stages/stage32/residual-32-01-production/post1648al-beauville-cover-projection-genus-bound.json": "dbe2bea1b2cae1e69ad6c27e5828f81494532fa4",
}

ZERO = (0, 0)
ONE = (1, 0)
MONE = (-1, 0)
I = (0, 1)
MI = (0, -1)


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def gmul(x, y):
    a, b = x
    c, d = y
    return (a * c - b * d, a * d + b * c)


def gadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def gneg(x):
    return (-x[0], -x[1])


def gscale(e: int, x):
    return (e * x[0], e * x[1])


def pnormalize(p):
    for x in p:
        if x != ZERO:
            # every nonzero node coordinate is a Gaussian unit
            u = (x[0], -x[1])
            return tuple(gmul(u, y) for y in p)
    raise AssertionError("zero projective point")


def gen_images(p):
    a1, a2, a3, b1, b2, b3, c = p
    return (
        (a2, a1, a3, b2, b1, b3, c),
        (a3, a2, a1, b3, b2, b1, c),
        (gmul(I, c), a2, a3, b1, gmul(I, b3), gmul(MI, b2), gmul(MI, a1)),
        (gneg(a1), a2, a3, b1, b2, b3, c),
        (a1, gneg(a2), a3, b1, b2, b3, c),
        (a1, a2, gneg(a3), b1, b2, b3, c),
        (a1, a2, a3, gneg(b1), b2, b3, c),
        (a1, a2, a3, b1, gneg(b2), b3, c),
        (a1, a2, a3, b1, b2, gneg(b3), c),
    )


def nodes48():
    seed = (ONE, ZERO, ZERO, ZERO, ONE, ONE, ONE)
    seen = {pnormalize(seed)}
    queue = deque(seen)
    while queue:
        p = queue.popleft()
        for image in gen_images(p):
            z = pnormalize(image)
            if z not in seen:
                seen.add(z)
                queue.append(z)
    return tuple(sorted(seen))


def aut_generators(nodes):
    pos = {p: i for i, p in enumerate(nodes)}
    out = []
    for k in range(9):
        perm = tuple(pos[pnormalize(gen_images(p)[k])] for p in nodes)
        assert sorted(perm) == list(range(48))
        out.append(perm)
    return tuple(out)


def z(x):
    return x == ZERO


def known_curve_incidence_rows(nodes):
    rows = []

    # C1: 32 conics.  Exact equations copied from the source-locked upstream file.
    for e1, e2, e3 in itertools.product((1, -1), repeat=3):
        rows.append([z(p[0]) and z(gadd(p[1], gscale(e1, p[5]))) and z(gadd(p[2], gscale(e2, p[4]))) and z(gadd(p[3], gscale(e3, p[6]))) for p in nodes])
    for e1, e2, e3 in itertools.product((1, -1), repeat=3):
        rows.append([z(p[1]) and z(gadd(p[2], gscale(e1, p[3]))) and z(gadd(p[0], gscale(e2, p[5]))) and z(gadd(p[4], gscale(e3, p[6]))) for p in nodes])
    for e1, e2, e3 in itertools.product((1, -1), repeat=3):
        rows.append([z(p[2]) and z(gadd(p[0], gscale(e1, p[4]))) and z(gadd(p[1], gscale(e2, p[3]))) and z(gadd(p[5], gscale(e3, p[6]))) for p in nodes])
    for e3, e2, e1 in itertools.product((1, -1), repeat=3):
        rows.append([z(p[6]) and z(gadd(gmul(I, p[0]), gscale(e1, p[3]))) and z(gadd(gmul(I, p[1]), gscale(e2, p[4]))) and z(gadd(gmul(I, p[2]), gscale(e3, p[5]))) for p in nodes])

    # C2: 12 boundary elliptics.
    for e1, e2 in itertools.product((1, -1), repeat=2):
        rows.append([z(p[3]) and z(gadd(gmul(I, p[1]), gscale(e1, p[2]))) and z(gadd(p[0], gscale(e2, p[6]))) for p in nodes])
    for e1, e2 in itertools.product((1, -1), repeat=2):
        rows.append([z(p[4]) and z(gadd(gmul(I, p[2]), gscale(e1, p[0]))) and z(gadd(p[1], gscale(e2, p[6]))) for p in nodes])
    for e1, e2 in itertools.product((1, -1), repeat=2):
        rows.append([z(p[5]) and z(gadd(gmul(I, p[0]), gscale(e1, p[1]))) and z(gadd(p[2], gscale(e2, p[6]))) for p in nodes])

    # C3: 48 other elliptics.  Node coordinates lie in Q(i).  An equation
    # sqrt(2)*x + eps*y=0 therefore forces x=y=0.
    for e1, _e2, e3 in itertools.product((1, -1), repeat=3):
        rows.append([z(gadd(p[0], gscale(e1, p[1]))) and z(p[0]) and z(p[5]) and z(gadd(p[3], gscale(e3, p[4]))) for p in nodes])
    for e1, _e2, e3 in itertools.product((1, -1), repeat=3):
        rows.append([z(gadd(p[1], gscale(e1, p[2]))) and z(p[1]) and z(p[3]) and z(gadd(p[4], gscale(e3, p[5]))) for p in nodes])
    for e1, _e2, e3 in itertools.product((1, -1), repeat=3):
        rows.append([z(gadd(p[2], gscale(e1, p[0]))) and z(p[2]) and z(p[4]) and z(gadd(p[5], gscale(e3, p[3]))) for p in nodes])
    for _e3, e2, e1 in itertools.product((1, -1), repeat=3):
        rows.append([z(gadd(gmul(I, p[0]), gscale(e1, p[6]))) and z(gadd(gmul(I, p[4]), gscale(e2, p[5]))) and z(p[0]) and z(p[3]) for p in nodes])
    for _e3, e2, e1 in itertools.product((1, -1), repeat=3):
        rows.append([z(gadd(gmul(I, p[1]), gscale(e1, p[6]))) and z(gadd(gmul(I, p[5]), gscale(e2, p[3]))) and z(p[1]) and z(p[4]) for p in nodes])
    for _e3, e2, e1 in itertools.product((1, -1), repeat=3):
        rows.append([z(gadd(gmul(I, p[2]), gscale(e1, p[6]))) and z(gadd(gmul(I, p[3]), gscale(e2, p[4]))) and z(p[2]) and z(p[5]) for p in nodes])

    assert len(rows) == 92
    return rows


def rowmask(row):
    x = 0
    for i, bit in enumerate(row):
        if bit:
            x |= 1 << i
    return x


def gf2_rank(vectors):
    pivots = {}
    for v in vectors:
        x = v
        while x:
            b = x.bit_length() - 1
            if b in pivots:
                x ^= pivots[b]
            else:
                pivots[b] = x
                break
    return len(pivots)


def permute_bits(x: int, perm):
    y = 0
    for old, new in enumerate(perm):
        if (x >> old) & 1:
            y |= 1 << new
    return y


def main():
    for rel, expected in LOCKS.items():
        assert git_blob_sha(ROOT / rel) == expected, rel

    mb103 = json.loads((ROOT / "stages/stage32/final-chain/32-03-multibranch/nodes/MB103/CERTIFICATE.json").read_text())
    al = json.loads((ROOT / "stages/stage32/residual-32-01-production/post1648al-beauville-cover-projection-genus-bound.json").read_text())
    cert = json.loads((NODE / "EVEN-SET-FAVORABLE-COVER-WALL.json").read_text())

    assert mb103["source_lock"]["upstream_commit"] == "51233ed5ef2bf228fac9416c66db9adc0ebcaadd"
    assert mb103["source_lock"]["upstream_blob_sha1"] == "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
    assert al["source_locked_inputs"]["resolved_cover_branch_divisor_is_48_exceptional_lines"] is True
    assert al["proof_adapter"]["factor_quotient_genus_Y"] == 2

    nodes = nodes48()
    assert len(nodes) == 48
    gens = aut_generators(nodes)
    assert len(gens) == 9

    rows = known_curve_incidence_rows(nodes)
    assert set(sum(row) for row in rows[:32]) == {6}
    assert set(sum(row) for row in rows[32:44]) == {8}
    assert set(sum(row) for row in rows[44:]) == {4}
    masks = [rowmask(row) for row in rows]
    assert gf2_rank(masks) == 25
    assert 48 - gf2_rank(masks) == 23

    # Enumerate only weight-four words of the necessary parity supercode.
    weight4 = []
    for comb in itertools.combinations(range(48), 4):
        v = sum(1 << i for i in comb)
        if all((v & r).bit_count() % 2 == 0 for r in masks):
            weight4.append(v)
    assert len(weight4) == 12

    # The 12 candidates are one Aut(S)-orbit.
    orbit = {weight4[0]}
    queue = deque(orbit)
    while queue:
        v = queue.popleft()
        for perm in gens:
            w = permute_bits(v, perm)
            if w not in orbit:
                orbit.add(w)
                queue.append(w)
    assert orbit == set(weight4)
    assert gf2_rank(orbit) == 12

    # The actual code has dimension b1(X)+1=2*q(X)+1=9.
    qX = 2 + 2
    b1X = 2 * qX
    actual_dim = b1X + 1
    assert qX == 4 and b1X == 8 and actual_dim == 9
    assert gf2_rank(orbit) > actual_dim

    # Hence weight 4 is impossible in the actual Aut-stable code; since the
    # all-48 word is actual, weight 44 is impossible by complement.
    assert cert["weight4_obstruction"]["actual_weight4_word_exists"] is False
    assert cert["weight44_obstruction"]["actual_weight44_word_exists"] is False

    # Double-cover invariants after blowing down the ramification (-1)-curves.
    favorable = []
    for w in range(0, 49, 4):
        K2 = 32
        c2 = 160 - 3 * w
        chi = 16 - w // 4
        assert (K2 + c2) // 12 == chi
        if K2 > c2:
            favorable.append(w)
    assert favorable == [44, 48]
    assert cert["double_cover_invariants"]["possible_weights_in_0_to_48_under_4_divisibility"] == favorable
    assert cert["double_cover_invariants"]["weight44_available"] is False
    assert cert["double_cover_invariants"]["weight48_is_existing_Beauville_cover"] is True
    assert cert["double_cover_invariants"]["distinct_favorable_Chern_even_subset_cover_exists"] is False

    decision = cert["decision"]
    assert decision["retire_distinct_even_subset_K2_gt_c2_cover_amplification_route"] is True
    assert decision["finite_degree_window_proved"] is False

    fw = cert["firewalls"]
    assert fw["necessary_parity_supercode_equals_actual_even_set_code"] is False
    assert fw["full_actual_code_reconstructed"] is False
    assert fw["finite_picard_enumeration_released"] is False
    assert fw["receiver_credit"] is False
    assert fw["merge_authorized"] is False

    print("MB104 even-set favorable-cover wall verifier PASS")
    print("necessary parity supercode: [48,23], incidence rank 25")
    print("weight-4 candidates: 12, one Aut(S) orbit, orbit-span rank 12")
    print("actual even-set code dimension: 9 => no actual weight 4 or 44")
    print("K^2>c2 even-subset weights: 44 or 48; only existing full-48 Beauville cover remains")
    print("finite degree window remains OPEN")


if __name__ == "__main__":
    main()
