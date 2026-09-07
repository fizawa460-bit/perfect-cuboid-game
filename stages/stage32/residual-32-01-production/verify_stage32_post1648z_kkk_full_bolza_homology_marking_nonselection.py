#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
CERT_PATH = HERE / "post1648z-kkk-full-bolza-homology-marking-nonselection.json"
EXPECTED_CERT_CANONICAL = "b8db79100ebc404a497e64e973fce7f631f6475b3fc220c32874f07095a6576e"

LOCKS = {
    "post1648Y": (HERE / "post1648y-cecotti-kkk-literal-branch-anchor-subsumption.json", "b170768b775fffc85e39c27c62193231c9e6f77f"),
    "post1648N": (HERE / "post1648n-canonical-period-marked-ppav-torsor-obstruction.json", "0ee05f679c7706113feed2c217e08a95b3bd6f06"),
    "post1648U": (HERE / "post1648u-kkk-delta0inf-explicit-half-period-nonpruning.json", "4151d5644b264f1ff1fd175f4fb1652354458d95"),
    "post1648S": (HERE / "post1648s-inner-conjugacy-invariant-nonselection-theorem.json", "a452fffad42516feaadf3ad44852bdc5c4f3090e"),
    "principal_rosati": (HERE / "post1490-o210-q4-bolza-principal-rosati-lock.json", "e28c4533883440ea0963d4d4e8859aa95409cf10"),
    "source_note": (HERE / "post1648z-kkk-full-bolza-homology-marking-nonselection-source-note.md", "4d1389d3979acc0582ba79956c48827962150f0b"),
}


def canonical_sha(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def mm(A, B):
    n, k, m = len(A), len(B), len(B[0])
    return [[sum(A[i][t] * B[t][j] for t in range(k)) for j in range(m)] for i in range(n)]


def mt(A):
    return [list(row) for row in zip(*A)]


def eye(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def det4(M):
    total = 0
    for p in itertools.permutations(range(4)):
        inv = sum(1 for i in range(4) for j in range(i + 1, 4) if p[i] > p[j])
        term = 1
        for i in range(4):
            term *= M[i][p[i]]
        total += (-1 if inv % 2 else 1) * term
    return total


def inv_unimod(M):
    n = 4
    aug = [[Fraction(M[i][j]) for j in range(n)] + [Fraction(1 if i == j else 0) for j in range(n)] for i in range(n)]
    for c in range(n):
        pivot = next(i for i in range(c, n) if aug[i][c] != 0)
        aug[c], aug[pivot] = aug[pivot], aug[c]
        q = aug[c][c]
        aug[c] = [x / q for x in aug[c]]
        for i in range(n):
            if i == c:
                continue
            q = aug[i][c]
            if q:
                aug[i] = [aug[i][j] - q * aug[c][j] for j in range(2 * n)]
    out = [[aug[i][n + j] for j in range(n)] for i in range(n)]
    assert all(x.denominator == 1 for row in out for x in row)
    return [[int(x) for x in row] for row in out]


def pair_mul(x, y):
    return (x[0] * y[0] - 2 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def pair_sub(x, y):
    return (x[0] - y[0], x[1] - y[1])


def real_matrix(entries):
    alpha, beta, gamma, delta = entries
    aa, ab = alpha
    ba, bb = beta
    ca, cb = gamma
    da, db = delta
    return [
        [aa, ba, -2 * ab, -2 * bb],
        [ca, da, -2 * cb, -2 * db],
        [ab, bb, aa, ba],
        [cb, db, ca, da],
    ]


def key(M):
    return tuple(x for row in M for x in row)


def from_key(t):
    return [list(t[4 * i:4 * i + 4]) for i in range(4)]


def close_group(generators):
    I = eye(4)
    seen = {key(I): I}
    queue = [I]
    while queue:
        X = queue.pop(0)
        for g in generators:
            Y = mm(X, g)
            k = key(Y)
            if k not in seen:
                seen[k] = Y
                queue.append(Y)
    return seen


def mod2_vec(M, v):
    return tuple(sum(M[i][j] * v[j] for j in range(4)) % 2 for i in range(4))


def main():
    cert = json.loads(CERT_PATH.read_text(encoding="utf-8"))
    assert canonical_sha(cert) == EXPECTED_CERT_CANONICAL
    assert cert["canonical_sha256_without_this_field"] == EXPECTED_CERT_CANONICAL

    for _, (path, expected_blob) in LOCKS.items():
        assert git_blob_sha(path) == expected_blob

    rosati = json.loads(LOCKS["principal_rosati"][0].read_text(encoding="utf-8"))
    E = rosati["principal_polarization"]["riemann_form_matrix"]
    source_form = [
        [0, 0, -1, 0],
        [0, 0, 0, -1],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
    ]
    C2 = [
        [-1, 1, 2, 0],
        [1, -1, 0, 2],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
    ]

    els = [(a, b) for a in range(-2, 3) for b in range(-2, 3)]
    valid = []
    for alpha, beta, gamma, delta in itertools.product(els, repeat=4):
        determinant = pair_sub(pair_mul(alpha, delta), pair_mul(beta, gamma))
        if determinant not in ((2, 0), (-2, 0)):
            continue
        R = real_matrix((alpha, beta, gamma, delta))
        M2 = mm(R, C2)
        if any(x % 2 for row in M2 for x in row):
            continue
        M = [[x // 2 for x in row] for row in M2]
        if abs(det4(M)) != 1:
            continue
        if mm(mm(mt(M), E), M) != source_form:
            continue
        valid.append(M)
    assert len(valid) == 48
    assert len({key(M) for M in valid}) == 48

    S = real_matrix(((1, 0), (1, 1), (0, 0), (-1, 0)))
    T = real_matrix(((1, 0), (1, 0), (-1, 0), (0, 0)))
    G = close_group((S, T))
    assert len(G) == 48

    mats = cert["source_homology_marking"]["displayed_cycle_action_matrices"]
    source_actions = [mt(mats[name]) for name in ("mu1", "mu2", "mu3")]

    lines = {
        "L1": (0, 0, 1, 0),
        "L2": (0, 0, 0, 1),
        "L3": (0, 0, 1, 1),
    }
    delta = (0, 0, 1, 1)
    line_counts = {name: 0 for name in lines}
    distinct = {}

    for M in valid:
        Minv = inv_unimod(M)
        target_actions = [mm(mm(M, A), Minv) for A in source_actions]
        assert all(key(A) in G for A in target_actions)
        triple = tuple(key(A) for A in target_actions)
        distinct[triple] = distinct.get(triple, 0) + 1

        image_delta = mod2_vec(M, delta)
        matched = [name for name, v in lines.items() if image_delta == v]
        assert len(matched) == 1
        line_counts[matched[0]] += 1

    assert len(distinct) == 24
    assert set(distinct.values()) == {2}
    assert line_counts == {"L1": 16, "L2": 16, "L3": 16}

    rep = next(iter(distinct))
    stabilizer = []
    for g in G.values():
        gi = inv_unimod(g)
        if all(key(mm(mm(g, from_key(t)), gi)) == t for t in rep):
            stabilizer.append(g)
    assert len(stabilizer) == 2
    minusI = [[-1 if i == j else 0 for j in range(4)] for i in range(4)]
    assert {key(x) for x in stabilizer} == {key(eye(4)), key(minusI)}

    exact = cert["exact_replay"]
    assert exact["polarized_period_lattice_isomorphisms_replayed"] == 48
    assert exact["all_three_conjugated_generators_land_in_retained_G12_for_every_isomorphism"] is True
    assert exact["distinct_ordered_target_generator_triples"] == 24
    assert exact["multiplicity_per_target_triple"] == 2
    assert exact["triple_stabilizer_size"] == 2
    assert exact["triple_stabilizer_identified_with_center_pmI"] is True
    assert exact["delta0inf_target_line_counts"] == line_counts
    assert exact["absolute_W_line_selected"] is False

    decision = cert["decision"]
    assert decision["absolute_delta0inf_retained_W_line_identified"] is False
    assert decision["survivors_current_credit"] == [73, 97, 235]
    assert decision["Q602_excluded"] is False
    assert decision["O210_excluded"] is False
    assert cert["firewalls"]["scratch_result_promoted_to_MAIN_authority"] is False
    assert cert["firewalls"]["scratch_result_promoted_to_current_credit"] is False

    print("POST1648Z_KKK_FULL_BOLZA_HOMOLOGY_MARKING_NONSELECTION_COMPLETE")
    print("polarized_period_lattice_isomorphisms=48")
    print("distinct_target_generator_triples=24 multiplicity_each=2 stabilizer=center_pmI")
    print("delta0inf_target_line_counts=L1:16,L2:16,L3:16")
    print("absolute_delta0inf_retained_W_line_identified=false")
    print("survivors=73,97,235 Q602_excluded=false O210_excluded=false")


if __name__ == "__main__":
    main()
