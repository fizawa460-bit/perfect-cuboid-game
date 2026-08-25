#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
import pathlib
import subprocess

EXPECTED_CORE_SHA = "de84f4511ea2ea747fd712e2f5f09c7f8d94ae3633e55678b81cfe63f6ed2870"
EXPECTED_SOURCE_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"
N = 64
RANK = 63
M = 140


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode()
    ).hexdigest()


def egcd(a: int, b: int) -> tuple[int, int, int]:
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    if old_r < 0:
        old_r, old_s, old_t = -old_r, -old_s, -old_t
    return old_r, old_s, old_t


def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    bt = list(zip(*b))
    return [[sum(x * y for x, y in zip(row, col)) for col in bt] for row in a]


def transpose(a: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*a)]


def row_times_matrix(row: list[int], matrix: list[list[int]]) -> list[int]:
    return [sum(row[i] * matrix[i][j] for i in range(len(row))) for j in range(len(matrix[0]))]


def kernel_basis_primitive_row(row: list[int]) -> tuple[list[list[int]], int]:
    n = len(row)
    g_all = 0
    for value in row:
        g_all = math.gcd(g_all, abs(value))
    assert g_all > 0
    primitive = [value // g_all for value in row]
    r = primitive[:]
    v = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
    pivot = next(i for i, value in enumerate(r) if value)
    if pivot:
        for i in range(n):
            v[i][0], v[i][pivot] = v[i][pivot], v[i][0]
        r[0], r[pivot] = r[pivot], r[0]
    for j in range(1, n):
        if r[j] == 0:
            continue
        d, s, t = egcd(r[0], r[j])
        a, b = r[0], r[j]
        old0 = [v[i][0] for i in range(n)]
        oldj = [v[i][j] for i in range(n)]
        for i in range(n):
            v[i][0] = s * old0[i] + t * oldj[i]
            v[i][j] = (-b // d) * old0[i] + (a // d) * oldj[i]
        r[0] = d
        r[j] = 0
    assert abs(r[0]) == 1 and all(value == 0 for value in r[1:])
    basis = [[v[i][j] for j in range(1, n)] for i in range(n)]
    assert all(value == 0 for value in row_times_matrix(primitive, basis))
    return basis, g_all


def gp_matrix(matrix: list[list[int]]) -> str:
    return "[" + ";".join(",".join(str(v) for v in row) for row in matrix) + "]"


def parse_vec(text: str) -> list[int]:
    text = text.strip()
    assert text.startswith("[") and text.endswith("]")
    body = text[1:-1].strip()
    return [] if not body else [int(x.strip()) for x in body.split(",")]


def pari_lll_transform(q: list[list[int]]) -> list[list[int]]:
    code = f"""
Q={gp_matrix(q)};
T=qflllgram(Q,1);
print("META|",matsize(T)[1],"|",matsize(T)[2]);
for(i=1,matsize(T)[1],print("R|",i,"|",Vec(T[i,])));
quit;
"""
    proc = subprocess.run(["gp", "-q"], input=code, text=True, capture_output=True, check=False)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr[-4000:])
    rows: list[list[int]] = []
    meta = None
    for raw in proc.stdout.splitlines():
        line = raw.strip()
        if line.startswith("META|"):
            _, a, b = line.split("|", 2)
            meta = (int(a), int(b))
        elif line.startswith("R|"):
            _, _, payload = line.split("|", 2)
            rows.append(parse_vec(payload))
    assert meta == (RANK, RANK)
    assert len(rows) == RANK and all(len(row) == RANK for row in rows)
    return rows


def det_bareiss(a: list[list[int]]) -> int:
    a = [row[:] for row in a]
    n = len(a)
    sign = 1
    prev = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            swap = next((i for i in range(k + 1, n) if a[i][k] != 0), None)
            if swap is None:
                return 0
            a[k], a[swap] = a[swap], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * pivot - a[i][k] * a[k][j]) // prev
        prev = pivot
        for i in range(k + 1, n):
            a[i][k] = 0
    return sign * a[n - 1][n - 1]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--core", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    args = ap.parse_args()

    core = json.loads(args.core.read_text())
    unsigned = dict(core)
    claimed = unsigned.pop("canonical_sha256_without_this_field")
    assert claimed == EXPECTED_CORE_SHA == csha(unsigned)
    assert core["source"]["git_blob_sha1"] == EXPECTED_SOURCE_BLOB

    gram = [[int(v) for v in row] for row in core["basis_gram"]]
    h = [int(v) for v in core["hyperplane"]]
    known = [[int(v) for v in row] for row in core["raw_cross_pairings_with_basis"]]
    assert len(gram) == N and all(len(row) == N for row in gram)
    assert len(h) == N
    assert len(known) == M and all(len(row) == N for row in known)

    hrow = [sum(h[i] * gram[i][j] for i in range(N)) for j in range(N)]
    assert sum(hrow[i] * h[i] for i in range(N)) == 16
    basis, content = kernel_basis_primitive_row(hrow)
    assert content == 2
    assert all(v == 0 for v in row_times_matrix(hrow, basis))

    gb = matmul(gram, basis)
    q0 = [[-v for v in row] for row in matmul(transpose(basis), gb)]
    assert q0 == transpose(q0)
    assert all(q0[i][i] > 0 for i in range(RANK))

    t = pari_lll_transform(q0)
    det_t = det_bareiss(t)
    assert abs(det_t) == 1
    rbasis = matmul(basis, t)
    q = matmul(transpose(t), matmul(q0, t))
    assert q == transpose(q)
    assert all(q[i][i] > 0 for i in range(RANK))
    assert all(v == 0 for v in row_times_matrix(hrow, rbasis))

    p0 = [sum(row[i] * h[i] for i in range(N)) for row in known]
    lin = [row_times_matrix(row, rbasis) for row in known]
    caps = [8] * 92 + [4] * 48

    zero_ok = all(0 <= p0[i] <= caps[i] for i in range(M))
    assert zero_ok

    payload = {
        "core_sha": EXPECTED_CORE_SHA,
        "source_blob": EXPECTED_SOURCE_BLOB,
        "q": q,
        "p0": p0,
        "caps": caps,
        "lin": lin,
    }
    input_sha = csha(payload)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w") as f:
        f.write("S32_D16_CONSTRAINED_HPERP_V1\n")
        f.write(EXPECTED_CORE_SHA + "\n")
        f.write(EXPECTED_SOURCE_BLOB + "\n")
        f.write(input_sha + "\n")
        f.write(f"{RANK} {M}\n")
        for row in q:
            f.write(" ".join(map(str, row)) + "\n")
        for i in range(M):
            f.write(f"{p0[i]} {caps[i]} " + " ".join(map(str, lin[i])) + "\n")

    print(json.dumps({
        "rank": RANK,
        "constraints": M,
        "hrow_content": content,
        "lll_det": det_t,
        "q_diag_min": min(q[i][i] for i in range(RANK)),
        "q_diag_max": max(q[i][i] for i in range(RANK)),
        "zero_candidate_passes": zero_ok,
        "prepared_input_sha256": input_sha,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
