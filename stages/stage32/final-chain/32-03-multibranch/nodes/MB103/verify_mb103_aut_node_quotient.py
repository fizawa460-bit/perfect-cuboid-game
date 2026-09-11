#!/usr/bin/env python3
from __future__ import annotations

import json
from collections import deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = Path(__file__).with_name("CERTIFICATE.json")
STATE = ROOT / "STATE.json"

ZERO = (0, 0)
ONE = (1, 0)
MONE = (-1, 0)
I = (0, 1)
MI = (0, -1)


def gmul(x, y):
    a, b = x
    c, d = y
    return (a * c - b * d, a * d + b * c)


def gneg(x):
    return (-x[0], -x[1])


def unit_inv(x):
    assert x in (ONE, MONE, I, MI)
    return (x[0], -x[1])


def pnormalize(p):
    for x in p:
        if x != ZERO:
            u = unit_inv(x)
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


def gsquare(x):
    return gmul(x, x)


def gadd(*xs):
    return (sum(x[0] for x in xs), sum(x[1] for x in xs))


def gsub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def on_surface(p):
    a1, a2, a3, b1, b2, b3, c = p
    eqs = (
        gsub(gadd(gsquare(a1), gsquare(a2)), gsquare(b3)),
        gsub(gadd(gsquare(a2), gsquare(a3)), gsquare(b1)),
        gsub(gadd(gsquare(a1), gsquare(a3)), gsquare(b2)),
        gsub(gadd(gsquare(a1), gsquare(a2), gsquare(a3)), gsquare(c)),
    )
    return eqs == (ZERO, ZERO, ZERO, ZERO)


def orbit_nodes():
    # R1 is singular: the second Jacobian row vanishes there, while rows
    # 1,3,4 have independent b3,b2,c pivots, so the Jacobian rank is 3 < 4.
    seed = (ONE, ZERO, ZERO, ZERO, ONE, ONE, ONE)
    assert on_surface(seed)
    seen = {pnormalize(seed)}
    queue = deque(seen)
    while queue:
        p = queue.popleft()
        for img in gen_images(p):
            z = pnormalize(img)
            assert on_surface(z)
            if z not in seen:
                seen.add(z)
                queue.append(z)
    return tuple(sorted(seen))


def generators_on(nodes):
    pos = {p: i for i, p in enumerate(nodes)}
    out = []
    for k in range(9):
        perm = []
        for p in nodes:
            z = pnormalize(gen_images(p)[k])
            assert z in pos
            perm.append(pos[z])
        assert sorted(perm) == list(range(len(nodes)))
        out.append(tuple(perm))
    return tuple(out)


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def generated_group(gens, n):
    ident = tuple(range(n))
    seen = {ident}
    queue = deque([ident])
    while queue:
        g = queue.popleft()
        for s in gens:
            h = compose(s, g)
            if h not in seen:
                seen.add(h)
                queue.append(h)
    return tuple(seen)


def apply_profile(profile, perm):
    out = [None] * len(profile)
    for old, new in enumerate(perm):
        out[new] = profile[old]
    return tuple(out)


def canonical_profile(profile, group):
    profile = tuple(profile)
    return min(apply_profile(profile, g) for g in group)


def pair_orbit_sizes(group, n):
    unseen = {(i, j) for i in range(n) for j in range(i + 1, n)}
    sizes = []
    while unseen:
        a, b = min(unseen)
        orbit = set()
        for g in group:
            x, y = g[a], g[b]
            if x > y:
                x, y = y, x
            orbit.add((x, y))
        sizes.append(len(orbit))
        unseen.difference_update(orbit)
    return sorted(sizes)


def main():
    cert = json.loads(CERT.read_text())
    state = json.loads(STATE.read_text())

    assert cert["schema"] == "STAGE32_MB103_AUT_NODE_QUOTIENT_V1"
    assert cert["source_lock"]["upstream_commit"] == "51233ed5ef2bf228fac9416c66db9adc0ebcaadd"
    assert cert["source_lock"]["upstream_blob_sha1"] == "0422b69847f2afb97cb7b3ed02ebef91279f61b1"

    nodes = orbit_nodes()
    assert len(nodes) == 48
    gens = generators_on(nodes)
    assert len(gens) == 9
    group = generated_group(gens, 48)
    assert len(group) == 1536

    assert len({g[0] for g in group}) == 48
    assert len([g for g in group if g[0] == 0]) == 32

    pair_sizes = pair_orbit_sizes(group, 48)
    assert pair_sizes == [24, 48, 48, 48, 192, 384, 384]

    profile = tuple((i % 4, (3 * i) % 7, (5 * i) % 11) for i in range(48))
    key = canonical_profile(profile, group)
    for s in gens:
        assert canonical_profile(apply_profile(profile, s), group) == key

    # Histograms are not complete: choose representatives from two different
    # pair orbits and compare their binary marked-node profiles.
    unseen = {(i, j) for i in range(48) for j in range(i + 1, 48)}
    reps = []
    while unseen:
        a, b = min(unseen)
        orbit = set()
        for g in group:
            x, y = g[a], g[b]
            if x > y:
                x, y = y, x
            orbit.add((x, y))
        reps.append((a, b))
        unseen.difference_update(orbit)
    p1 = [0] * 48
    p2 = [0] * 48
    for i in reps[0]:
        p1[i] = 1
    for i in reps[-1]:
        p2[i] = 1
    assert sorted(p1) == sorted(p2)
    assert canonical_profile(tuple(p1), group) != canonical_profile(tuple(p2), group)

    action = cert["aut_node_action"]
    assert action["node_count"] == 48
    assert action["generator_count"] == 9
    assert action["group_order"] == 1536
    assert action["transitive_on_nodes"] is True
    assert action["point_stabilizer_order"] == 32
    assert action["unordered_pair_orbit_sizes"] == pair_sizes

    quotient = cert["quotient_contract"]
    assert quotient["exact_for_intrinsic_node_indexed_discrete_payload"] is True
    assert quotient["histogram_is_complete_orbit_invariant"] is False
    assert quotient["raw_lambda_coordinate_quotiented"] is False
    assert quotient["finite_degree_window_proved"] is False
    assert quotient["finite_picard_enumeration_released"] is False

    assert state["current_node"] == "MB104"
    assert "MB103" in state["completed_retained_nodes"]
    assert state["mb103"]["group_order"] == 1536
    assert state["mb103"]["receiver_credit"] is False

    print("MB103 verifier PASS")
    print("nodes=48 generators=9 |Aut_node|=1536 orbit=48 stabilizer=32")
    print("unordered_pair_orbits=" + ",".join(map(str, pair_sizes)))
    print("finite_window=false receiver_credit=false")


if __name__ == "__main__":
    main()
