#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
CERT_PATH = HERE / "post1648n-canonical-period-marked-ppav-torsor-obstruction.json"
ROSATI_PATH = HERE / "post1490-o210-q4-bolza-principal-rosati-lock.json"

EXPECTED_CERT_CANONICAL = "060d940626cd59b00efb67db7f27914e6a440c92968600a3d82a208d5a5d76ba"
EXPECTED_ROSATI_CANONICAL = "8d828cdf6d1f5cb1d790c46292535dc252e503356e1047ce972c41e61f524529"
EXPECTED_ROSATI_BLOB = "e28c4533883440ea0963d4d4e8859aa95409cf10"


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


def inv_unimodular(M):
    n = 4
    aug = [[Fraction(M[i][j]) for j in range(n)] +
           [Fraction(1 if i == j else 0) for j in range(n)] for i in range(n)]
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


def mat_key(M):
    return tuple(x for row in M for x in row)


def mat_mod2_vec(M, v):
    return tuple(sum(M[i][j] * v[j] for j in range(4)) % 2 for i in range(4))


def mat_pow(M, n):
    out = eye(4)
    for _ in range(n):
        out = mm(out, M)
    return out


def close_group(generators):
    I = eye(4)
    seen = {mat_key(I): I}
    words = {mat_key(I): "id"}
    queue = [I]
    while queue:
        X = queue.pop(0)
        w = words[mat_key(X)]
        for name, g in generators:
            Y = mm(X, g)
            k = mat_key(Y)
            if k not in seen:
                seen[k] = Y
                words[k] = name if w == "id" else w + "*" + name
                queue.append(Y)
    return seen, words


def main():
    cert = json.loads(CERT_PATH.read_text(encoding="utf-8"))
    assert canonical_sha(cert) == EXPECTED_CERT_CANONICAL
    assert cert["canonical_sha256_without_this_field"] == EXPECTED_CERT_CANONICAL

    rosati = json.loads(ROSATI_PATH.read_text(encoding="utf-8"))
    assert canonical_sha(rosati) == EXPECTED_ROSATI_CANONICAL
    assert rosati["canonical_sha256_without_this_field"] == EXPECTED_ROSATI_CANONICAL
    assert git_blob_sha(ROSATI_PATH) == EXPECTED_ROSATI_BLOB
    assert rosati["principal_polarization"]["riemann_form_basis"] == ["e1", "e2", "r*e1", "r*e2"]

    E = rosati["principal_polarization"]["riemann_form_matrix"]
    source_form = [
        [0, 0, -1, 0],
        [0, 0, 0, -1],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
    ]
    # 2 * coordinate matrix of [B | I] in the retained O^2 basis,
    # B=[[(-1+r)/2,1/2],[1/2,(-1+r)/2]].
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
    assert len({mat_key(M) for M in valid}) == 48

    # Retained G12 real-lattice action.
    S = real_matrix(((1, 0), (1, 1), (0, 0), (-1, 0)))  # b4
    T = real_matrix(((1, 0), (1, 0), (-1, 0), (0, 0)))  # -b3
    G, words = close_group((("S", S), ("T", T)))
    assert len(G) == 48

    # KKK (3.43) gives action on the ordered cycle basis itself.
    # Coordinate columns therefore transform by transpose.
    T_cycle = [
        [0, -1, 1, -1],
        [0, 1, 0, 1],
        [-1, 1, -1, 1],
        [-1, -1, 0, 0],
    ]
    mu_coord = mt(T_cycle)
    assert mat_pow(mu_coord, 8) == eye(4)
    assert mat_pow(mu_coord, 4) != eye(4)

    lines = {
        "L1": (0, 0, 1, 0),
        "L2": (0, 0, 0, 1),
        "L3": (0, 0, 1, 1),
    }
    fixed_counts = {k: 0 for k in lines}
    image_counts = {}
    word_by_line = {k: set() for k in lines}

    for M in valid:
        Minv = inv_unimodular(M)
        image = mm(mm(M, mu_coord), Minv)
        key = mat_key(image)
        assert key in G
        assert mat_pow(image, 8) == eye(4)
        assert mat_pow(image, 4) != eye(4)

        fixed = []
        for lname, v in lines.items():
            w = mat_mod2_vec(image, v)
            assert w[0] == 0 and w[1] == 0
            if w == v:
                fixed.append(lname)
        assert len(fixed) == 1
        lname = fixed[0]
        fixed_counts[lname] += 1
        image_counts[key] = image_counts.get(key, 0) + 1
        word_by_line[lname].add(words[key])

    assert len(image_counts) == 6
    assert set(image_counts.values()) == {8}
    assert fixed_counts == {"L1": 16, "L2": 16, "L3": 16}
    assert {k: sorted(v) for k, v in word_by_line.items()} == {
        "L1": ["S*T*S*T*S", "T*S*T"],
        "L2": ["S*T*T", "T*S"],
        "L3": ["S*T", "T*T*S"],
    }

    exact = cert["exact_enumeration"]
    assert exact["principal_polarization_maps_found"] == 48
    assert exact["distinct_target_mu1_images"] == 6
    assert exact["isomorphisms_per_target_mu1_image"] == 8
    assert exact["delta0inf_fixed_line_counts"] == fixed_counts

    decision = cert["decision"]
    assert decision["absolute_delta0inf_retained_W_line_identified"] is False
    assert decision["survivors_current_credit"] == [73, 97, 235]
    assert decision["Q602_excluded"] is False
    assert decision["O210_excluded"] is False
    assert cert["firewalls"]["scratch_result_promoted_to_MAIN_authority"] is False
    assert cert["firewalls"]["scratch_result_promoted_to_current_credit"] is False

    print("POST1648N_CANONICAL_PERIOD_MARKED_PPAV_TORSOR_OBSTRUCTION_COMPLETE")
    print("polarized_period_lattice_isomorphisms=48 exhaustive_by_ppav_torsor=true")
    print("target_mu1_order8_images=6 multiplicity_each=8")
    print("delta0inf_fixed_line_counts=L1:16,L2:16,L3:16")
    print("absolute_delta0inf_retained_W_line_identified=false")
    print("survivors=73,97,235 Q602_excluded=false O210_excluded=false")


if __name__ == "__main__":
    main()
