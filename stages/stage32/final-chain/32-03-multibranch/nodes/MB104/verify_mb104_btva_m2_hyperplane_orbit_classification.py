#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CERT = HERE / "BTVA-M2-HYPERPLANE-ORBIT-CLASSIFICATION.json"
FULLMAP = HERE / "BTVA-FULL-M2-NODE-EXTENSION-MAP.json"
MB103 = ROOT / "nodes" / "MB103" / "verify_mb103_aut_node_quotient.py"

P = 1097
IR = 341


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def load_mb103():
    spec = importlib.util.spec_from_file_location("mb103_verify", MB103)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def modg(x):
    return (x[0] + IR * x[1]) % P


def inv(a):
    return pow(a % P, P - 2, P)


def rank_mod(rows):
    a = [[int(x) % P for x in row] for row in rows]
    if not a:
        return 0
    m, n = len(a), len(a[0])
    r = 0
    for c in range(n):
        piv = next((i for i in range(r, m) if a[i][c]), None)
        if piv is None:
            continue
        a[r], a[piv] = a[piv], a[r]
        z = inv(a[r][c])
        a[r] = [(x * z) % P for x in a[r]]
        for i in range(m):
            if i != r and a[i][c]:
                f = a[i][c]
                a[i] = [(x - f * y) % P for x, y in zip(a[i], a[r])]
        r += 1
        if r == m:
            break
    return r


def mmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) % P
             for j in range(len(b[0]))]
            for i in range(len(a))]


def action12():
    a = [[0] * 13 for _ in range(13)]
    for j, (i, s) in enumerate(((1, 1), (0, 1), (3, 1), (2, 1), (4, 1), (5, -1))):
        a[i][j] = s % P
    for j, i in enumerate((1, 0, 2, 4, 3, 5, 6)):
        a[6 + i][6 + j] = 1
    return a


def action13():
    a = [[0] * 13 for _ in range(13)]
    for j, (i, s) in enumerate(((4, -1), (1, 1), (2, -1), (5, -1), (0, -1), (3, -1))):
        a[i][j] = s % P
    for j, i in enumerate((2, 1, 0, 5, 4, 3, 6)):
        a[6 + i][6 + j] = 1
    return a


def chart_map(pt):
    x1, x2, x3, y1, y2, y3, z = pt
    assert x1 == 1
    M = [[0] * 13 for _ in range(3)]
    if x2 == x3 == y1 == 0:
        cols = ((0, 0, 0), (0, -2, 0), (z, 0, -z), (0, 0, 0),
                (1, 0, -1), (0, 2 * z, 0))
        eta = (y2 * y3 % P, 0, y2 * y3 % P)
    elif y3 == z == x3 == 0:
        a, b, e = x2, y1, y2
        cols = ((-a, 0, a), (1, 0, -1), (a, 0, a), (-1, 0, -1),
                (0, 0, 0), (0, 0, 0))
        eta = (0, 2 * b * e, 0)
    elif y2 == z == x2 == 0:
        a, b, e = x3, y1, y3
        cols = ((-a, 0, a), (0, 0, 0), (0, 0, 0), (1, 0, 1),
                (-1, 0, 1), (a, 0, a))
        eta = (0, 2 * b * e, 0)
    else:
        raise AssertionError(f"unexpected x1-chart node {pt}")
    for j, col in enumerate(cols):
        for r in range(3):
            M[r][j] = col[r] % P
    for j, val in enumerate(pt, start=6):
        for r in range(3):
            M[r][j] = val * eta[r] % P
    return M


def build_maps(mb103, nodes):
    pos = {p: i for i, p in enumerate(nodes)}
    pts = [tuple(modg(x) for x in p) for p in nodes]
    a12, a13 = action12(), action13()
    chart = {i: chart_map(pts[i]) for i, p in enumerate(nodes) if p[0] != mb103.ZERO}
    out = []
    overlap = 0
    for i, p in enumerate(nodes):
        if p[0] != mb103.ZERO:
            M = chart[i]
        else:
            choices = []
            if p[1] != mb103.ZERO:
                q = mb103.pnormalize(mb103.gen_images(p)[0])
                choices.append(mmul(chart[pos[q]], a12))
            if p[2] != mb103.ZERO:
                q = mb103.pnormalize(mb103.gen_images(p)[1])
                choices.append(mmul(chart[pos[q]], a13))
            assert choices
            if len(choices) == 2:
                overlap += 1
                assert rank_mod(choices[0] + choices[1]) == 3
            M = choices[0]
        assert rank_mod(M) == 3
        out.append(M)
    assert overlap == 8
    assert rank_mod([row for M in out for row in M]) == 13
    return out


def rows_for_mask(mask, maps):
    return [row for i, M in enumerate(maps) if (mask >> i) & 1 for row in M]


def apply_mask(mask, perm):
    out = 0
    for old in range(48):
        if (mask >> old) & 1:
            out |= 1 << perm[old]
    return out


def main():
    cert = json.loads(CERT.read_text())
    parent = json.loads(FULLMAP.read_text())
    assert cert["schema"] == "STAGE32_MB104_BTVA_M2_HYPERPLANE_ORBIT_CLASSIFICATION_V2"
    assert parent["schema"] == "STAGE32_MB104_BTVA_FULL_M2_NODE_EXTENSION_MAP_V1"
    assert git_blob_sha1(FULLMAP) == cert["parents"]["full_m2_map_blob_sha1"]
    assert git_blob_sha1(MB103) == cert["parents"]["mb103_verifier_blob_sha1"]
    assert cert["source_locks"]["btva_transcript_rank6_span_count"] == 593735
    assert cert["source_locks"]["btva_transcript_hyperplane_orbit_count"] == 2442

    mb103 = load_mb103()
    nodes = mb103.orbit_nodes()
    assert len(nodes) == 48
    gens = mb103.generators_on(nodes)
    group = mb103.generated_group(gens, 48)
    assert len(group) == 1536
    maps = build_maps(mb103, nodes)

    hinfo = cert["hyperplanes"]["rank11_aut_orbits"]
    all_h = set()
    for h in hinfo:
        mask = h["rep_mask"]
        assert rank_mod(rows_for_mask(mask, maps)) == 11
        orbit = {apply_mask(mask, g) for g in group}
        assert len(orbit) == h["orbit_size"]
        assert not (all_h & orbit)
        all_h |= orbit
    assert len(all_h) == 3264
    assert sorted(h["orbit_size"] for h in hinfo) == [192, 384, 384, 384, 384, 768, 768]

    # Representative special section: (1,-i,-1,i,i,1,0,...,0).
    s = [1, (-IR) % P, -1 % P, IR, IR, 1] + [0] * 7
    support = 0
    for i, M in enumerate(maps):
        vals = [sum(row[j] * s[j] for j in range(13)) % P for row in M]
        if vals == [0, 0, 0]:
            support |= 1 << i
    special = cert["special_web_support_residual"]
    assert support == special["representative_mask"]
    assert support.bit_count() == 16
    assert [i for i in range(48) if (support >> i) & 1] == special["representative_node_indices_zero_based"]
    support_orbit = {apply_mask(support, g) for g in group}
    assert len(support_orbit) == 24

    # Every rank-11 representative is contained in this special support.
    # Exactly the remaining special-support nodes leave a one-dimensional kernel.
    survivor_pairs = set()
    for h in hinfo:
        mask = h["rep_mask"]
        assert mask & ~support == 0
        expected = support & ~mask
        assert expected.bit_count() == h["outside_rank12_survivors_per_hyperplane"]
        for p in range(48):
            if (mask >> p) & 1:
                continue
            r = rank_mod(rows_for_mask(mask, maps) + maps[p])
            if (expected >> p) & 1:
                assert r == 12
            else:
                assert r == 13
        for p in range(48):
            if (expected >> p) & 1:
                for g in group:
                    survivor_pairs.add((apply_mask(mask, g), g[p]))

    assert len(survivor_pairs) == cert["outside_pairs"]["extension_rank_distribution"]["12"] == 28416

    # Reconstruct the 35 survivor pair-orbits.
    unseen = set(survivor_pairs)
    orbit_sizes = []
    while unseen:
        mask, p0 = min(unseen)
        orbit = {(apply_mask(mask, g), g[p0]) for g in group}
        assert orbit <= survivor_pairs
        orbit_sizes.append(len(orbit))
        unseen.difference_update(orbit)
    assert len(orbit_sizes) == cert["outside_pairs"]["rank12_survivor_pair_orbit_count"] == 35
    assert Counter(orbit_sizes) == Counter({384: 12, 768: 15, 1536: 8})

    assert cert["outside_pairs"]["count"] == 24538032
    assert cert["outside_pairs"]["extension_rank_distribution"]["13"] == 24509616
    assert 24509616 + 28416 == 24538032

    full = cert["full_span_capacity"]
    assert full["simultaneous_m2_extension_kernel_dimension_upper_bound"] == 1
    assert full["if_nonzero_support_contained_in_special_24_residual"] is True
    assert full["if_nonzero_kernel_is_corresponding_special_section"] is True
    assert cert["decision"]["all_full_span_nonzero_m2_kernels_classified_into_special_24_residual"] is True
    assert cert["decision"]["population_wide_finite_degree_window_proved"] is False
    assert cert["firewalls"]["receiver_credit"] is False

    print("MB104 BTVA m=2 hyperplane/orbit verifier PASS")
    print("rank11_hyperplanes=3264 aut_orbits=7")
    print("outside_rank12_pairs=28416 pair_orbits=35")
    print("special_extension_supports=24 each_size=16")
    print("full_span_nonzero_m2_kernel => special_24_residual")
    print("finite_window=false receiver_credit=false")


if __name__ == "__main__":
    main()
