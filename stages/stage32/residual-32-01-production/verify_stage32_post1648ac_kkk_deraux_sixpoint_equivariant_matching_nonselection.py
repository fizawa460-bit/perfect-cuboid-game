#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT = HERE / "post1648ac-kkk-deraux-sixpoint-equivariant-matching-nonselection.json"
NOTE = HERE / "post1648ac-kkk-deraux-sixpoint-equivariant-matching-nonselection-source-note.md"
AB = HERE / "post1648ab-popov-k12-affine-class-pointwise-nonselection.json"
AA = HERE / "post1648aa-deraux-weierstrass-orbit-b9-fixed-pair-nonselection.json"
Z = HERE / "post1648z-kkk-full-bolza-homology-marking-nonselection.json"

EXPECTED_CANONICAL = "b04491c310cae6427511c58a76eed9fc166ad8f43c86a1d140d46b60f5f46a3f"
EXPECTED_NOTE_BLOB = "d2b68b248d3a489a7d6cbde75915ed6c8db7d053"
EXPECTED_AB_BLOB = "9cbd036d5a3a342f88215f935e2cbf159e90f6f4"
EXPECTED_AB_CANONICAL = "84ce4096aac5adf829df9bf001a28b7b92a7e0e513d122e5f55ce49b77825874"
EXPECTED_AA_BLOB = "c989058beb079cc36fb1d52f58707986e8b4320b"
EXPECTED_AA_CANONICAL = "a0ca0342db4902e737f28aa5f0de447cca2a2fce71f8cf0cdd2775d51804f7c7"
EXPECTED_Z_BLOB = "da3d30630698fc77098b3316c4ea4f19bc8258ef"
EXPECTED_Z_CANONICAL = "b8db79100ebc404a497e64e973fce7f631f6475b3fc220c32874f07095a6576e"


def canonical_sha(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def R(a=0, b=0):
    return (Fraction(a), Fraction(b))


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def mul(x, y):
    return (x[0] * y[0] - 2 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def mm2(A, B):
    return [[add(mul(A[i][0], B[0][j]), mul(A[i][1], B[1][j])) for j in range(2)] for i in range(2)]


def mv2(A, v):
    return [add(mul(A[i][0], v[0]), mul(A[i][1], v[1])) for i in range(2)]


def red(x):
    return (x[0] % 1, x[1] % 1)


ZERO = R()
ONE = R(1)
I2 = [[ONE, ZERO], [ZERO, ONE]]
ID = (I2, [ZERO, ZERO])


def compose(f, g):
    A, t = f
    B, u = g
    AB = mm2(A, B)
    Au = mv2(A, u)
    return AB, [red(add(Au[i], t[i])) for i in range(2)]


def key_affine(f):
    A, t = f
    return (
        tuple(tuple(tuple(e) for e in row) for row in A),
        tuple(red(x) for x in t),
    )


R1 = (
    [[R(1), R(0)], [R(1, -1), R(-1)]],
    [R(0), R(0)],
)
R2 = (
    [[R(-1, 1), R(2)], [R(1, 1), R(1, -1)]],
    [R(0), R(0)],
)
R3 = (
    [[R(1), R(-1, -1)], [R(0), R(-1)]],
    [R(Fraction(1, 2), Fraction(1, 2)), R(1)],
)
GENS = (R1, R2, R3)


def close_affine_group():
    seen = {key_affine(ID): ID}
    queue = [ID]
    while queue:
        f = queue.pop(0)
        for g in GENS:
            h = compose(f, g)
            k = key_affine(h)
            if k not in seen:
                seen[k] = h
                queue.append(h)
    return list(seen.values())


def ring_mul_mod2(x, y):
    a, b = x
    c, d = y
    return ((a * c) % 2, (a * d + b * c) % 2)


def act_bits(f, v):
    A, t = f
    z = [(v[0], v[2]), (v[1], v[3])]
    out = []
    for i in range(2):
        s = (0, 0)
        for j in range(2):
            a = (int(A[i][j][0]) % 2, int(A[i][j][1]) % 2)
            p = ring_mul_mod2(a, z[j])
            s = ((s[0] + p[0]) % 2, (s[1] + p[1]) % 2)
        ta = int(2 * t[i][0]) % 2
        tb = int(2 * t[i][1]) % 2
        out.append(((s[0] + ta) % 2, (s[1] + tb) % 2))
    return (out[0][0], out[1][0], out[0][1], out[1][1])


def perm_comp(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def perm_inv(p):
    out = [None] * len(p)
    for i, j in enumerate(p):
        out[j] = i
    return tuple(out)


def close_perm(gens):
    I = tuple(range(len(gens[0])))
    seen = {I}
    queue = [I]
    while queue:
        x = queue.pop(0)
        for g in gens:
            y = perm_comp(x, g)
            if y not in seen:
                seen.add(y)
                queue.append(y)
    return seen


def xor(u, v):
    return tuple(a ^ b for a, b in zip(u, v))


def main():
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    assert canonical_sha(cert) == EXPECTED_CANONICAL
    assert cert["canonical_sha256_without_this_field"] == EXPECTED_CANONICAL
    assert git_blob_sha(NOTE) == EXPECTED_NOTE_BLOB

    for path, blob, canonical in (
        (AB, EXPECTED_AB_BLOB, EXPECTED_AB_CANONICAL),
        (AA, EXPECTED_AA_BLOB, EXPECTED_AA_CANONICAL),
        (Z, EXPECTED_Z_BLOB, EXPECTED_Z_CANONICAL),
    ):
        obj = json.loads(path.read_text(encoding="utf-8"))
        assert git_blob_sha(path) == blob
        assert canonical_sha(obj) == canonical

    source_gens = (
        (0, 1, 4, 5, 3, 2),
        (3, 2, 1, 0, 5, 4),
        (1, 0, 3, 2, 4, 5),
    )
    source_group = close_perm(source_gens)
    assert len(source_group) == 24

    group = close_affine_group()
    assert len(group) == 48

    target_points = (
        (0, 0, 1, 0),
        (0, 0, 1, 1),
        (1, 0, 0, 0),
        (1, 0, 1, 1),
        (1, 1, 0, 1),
        (1, 1, 1, 1),
    )
    target_index = {v: i for i, v in enumerate(target_points)}
    target_group = {
        tuple(target_index[act_bits(f, v)] for v in target_points)
        for f in group
    }
    assert len(target_group) == 24

    surviving = []
    for phi in itertools.permutations(range(6)):
        inv = perm_inv(phi)
        conjugated = {
            tuple(phi[p[inv[j]]] for j in range(6))
            for p in source_group
        }
        if conjugated == target_group:
            surviving.append(phi)
    assert len(surviving) == 48

    lines = {
        (0, 0, 1, 0): "L1",
        (0, 0, 0, 1): "L2",
        (0, 0, 1, 1): "L3",
    }
    counts = {"L1": 0, "L2": 0, "L3": 0}
    for phi in surviving:
        u = target_points[phi[0]]
        v = target_points[phi[1]]
        d = xor(u, v)
        assert d in lines
        counts[lines[d]] += 1
    assert counts == {"L1": 16, "L2": 16, "L3": 16}

    exact = cert["exact_equivariant_matching"]
    assert exact["all_bijections_tested"] == 720
    assert exact["surviving_equivariant_bijections"] == 48
    assert exact["target_pair_difference_counts"] == counts
    assert exact["absolute_W_line_selected"] is False

    decision = cert["decision"]
    assert decision["absolute_delta0inf_retained_W_line_identified"] is False
    assert decision["survivors_current_credit"] == [73, 97, 235]
    assert decision["Q602_excluded"] is False
    assert decision["O210_excluded"] is False
    assert cert["firewalls"]["scratch_result_promoted_to_MAIN_authority"] is False
    assert cert["firewalls"]["scratch_result_promoted_to_current_credit"] is False

    print("POST1648AC_KKK_DERAUX_SIXPOINT_EQUIVARIANT_MATCHING_COMPLETE")
    print("source_S4=24 target_affine_permutation_image=24")
    print("bijections_tested=720 equivariant_bijections=48")
    print("delta0inf_target_line_counts=L1:16,L2:16,L3:16")
    print("survivors=73,97,235 Q602_excluded=false O210_excluded=false")


if __name__ == "__main__":
    main()
