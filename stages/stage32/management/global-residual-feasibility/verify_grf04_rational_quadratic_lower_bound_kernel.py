#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
CERT = HERE / "GRF-04-RATIONAL-QUADRATIC-LOWER-BOUND-KERNEL.json"
GRF01 = HERE / "GRF-01-CONTRACT.json"
GRF01_DESIGN = HERE / "GRF-01-DESIGN.md"
GRF03 = HERE / "GRF-03-NORM-LADDER-RESIDUE-COLLAPSE.json"

EXPECTED_BLOBS = {
    GRF01: "a81ebccfa0e235fe33926e16a0bd67bfcb29cbc0",
    GRF01_DESIGN: "7daa489d182e52401df9300acfe9899759515078",
    GRF03: "d6777200cadb6809dc3b46374c8f714cb6ebd6cd",
}
EXPECTED_CERT_CANONICAL = "70e6ecdf4c79ee51e843aea043a34e3deb4ad913822537e973be82d2c961114c"
EXPECTED_GRF01_CANONICAL = "18ce801f45bd95fec8e0a2f6001eff9fd80a9b6f6b416ccc9190d3b37adc3c43"
EXPECTED_GRF03_CANONICAL = "b7ff04666b5a29f7cca5da4df0fd9076a6e785702b594bda602cb4085d45c15d"


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise RuntimeError(msg)


def blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def qmatrix(rows: list[list[int | Fraction]]) -> list[list[Fraction]]:
    return [[Fraction(x) for x in row] for row in rows]


def transpose(a: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*a)] if a else []


def matmul(a: list[list[Fraction]], b: list[list[Fraction]]) -> list[list[Fraction]]:
    if not a:
        return []
    req(bool(b), "matrix product with empty right factor")
    req(len(a[0]) == len(b), "matrix product shape mismatch")
    return [
        [
            sum((a[i][k] * b[k][j] for k in range(len(b))), Fraction(0))
            for j in range(len(b[0]))
        ]
        for i in range(len(a))
    ]


def matvec(a: list[list[Fraction]], x: list[Fraction]) -> list[Fraction]:
    return [sum((u * v for u, v in zip(row, x)), Fraction(0)) for row in a]


def dot(x: list[Fraction], y: list[Fraction]) -> Fraction:
    return sum((u * v for u, v in zip(x, y)), Fraction(0))


def determinant(a: list[list[Fraction]]) -> Fraction:
    n = len(a)
    if n == 0:
        return Fraction(1)
    req(all(len(row) == n for row in a), "determinant requires square matrix")
    m = [row[:] for row in a]
    out = Fraction(1)
    for c in range(n):
        pivot = next((r for r in range(c, n) if m[r][c]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != c:
            m[c], m[pivot] = m[pivot], m[c]
            out = -out
        p = m[c][c]
        out *= p
        for r in range(c + 1, n):
            if not m[r][c]:
                continue
            f = m[r][c] / p
            for j in range(c + 1, n):
                m[r][j] -= f * m[c][j]
    return out


def inverse(a: list[list[Fraction]]) -> list[list[Fraction]]:
    n = len(a)
    req(n > 0 and all(len(row) == n for row in a), "inverse requires nonempty square matrix")
    m = [
        a[i][:] + [Fraction(int(i == j)) for j in range(n)]
        for i in range(n)
    ]
    for c in range(n):
        pivot = next((r for r in range(c, n) if m[r][c]), None)
        req(pivot is not None, "singular matrix")
        m[c], m[pivot] = m[pivot], m[c]
        p = m[c][c]
        m[c] = [x / p for x in m[c]]
        for r in range(n):
            if r == c or not m[r][c]:
                continue
            f = m[r][c]
            m[r] = [m[r][j] - f * m[c][j] for j in range(2 * n)]
    return [row[n:] for row in m]


def is_spd(q: list[list[Fraction]]) -> bool:
    n = len(q)
    if n == 0 or any(len(row) != n for row in q):
        return False
    if any(q[i][j] != q[j][i] for i in range(n) for j in range(n)):
        return False
    return all(determinant([row[:k] for row in q[:k]]) > 0 for k in range(1, n + 1))


def reduce_constraints(
    a: list[list[Fraction]], b: list[Fraction], n: int
) -> tuple[str, list[list[Fraction]], list[Fraction]]:
    req(len(a) == len(b), "constraint row/rhs mismatch")
    req(all(len(row) == n for row in a), "constraint width mismatch")
    if not a:
        return "FEASIBLE", [], []

    m = [a[i][:] + [b[i]] for i in range(len(a))]
    row = 0
    for c in range(n):
        pivot = next((r for r in range(row, len(m)) if m[r][c]), None)
        if pivot is None:
            continue
        m[row], m[pivot] = m[pivot], m[row]
        p = m[row][c]
        m[row] = [x / p for x in m[row]]
        for r in range(len(m)):
            if r == row or not m[r][c]:
                continue
            f = m[r][c]
            m[r] = [m[r][j] - f * m[row][j] for j in range(n + 1)]
        row += 1
        if row == len(m):
            break

    for r in range(len(m)):
        if all(m[r][c] == 0 for c in range(n)) and m[r][n] != 0:
            return "LINEAR_CONSTRAINT_EMPTY", [], []

    keep = [r for r in range(len(m)) if any(m[r][c] != 0 for c in range(n))]
    a0 = [[m[r][c] for c in range(n)] for r in keep]
    b0 = [m[r][n] for r in keep]
    return "FEASIBLE", a0, b0


def schur_minimum(
    q_in: list[list[int | Fraction]],
    a_in: list[list[int | Fraction]],
    b_in: list[int | Fraction],
) -> dict[str, object]:
    q = qmatrix(q_in)
    req(is_spd(q), "Q must be symmetric positive definite")
    n = len(q)
    a = qmatrix(a_in)
    b = [Fraction(x) for x in b_in]
    status, a0, b0 = reduce_constraints(a, b, n)
    if status == "LINEAR_CONSTRAINT_EMPTY":
        return {"status": status}

    if not a0:
        return {
            "status": "FEASIBLE",
            "rho": Fraction(0),
            "v_star": [Fraction(0) for _ in range(n)],
            "A0": [],
            "b0": [],
        }

    q_inv = inverse(q)
    s = matmul(matmul(a0, q_inv), transpose(a0))
    req(is_spd(s), "Schur matrix must be positive definite on independent constraints")
    lam = matvec(inverse(s), b0)
    v_star = matvec(matmul(q_inv, transpose(a0)), lam)
    rho = dot(b0, lam)
    req(matvec(a0, v_star) == b0, "computed minimizer is not feasible")
    req(rho == dot(v_star, matvec(q, v_star)), "minimum identity drift")
    return {"status": "FEASIBLE", "rho": rho, "v_star": v_star, "A0": a0, "b0": b0}


def qnorm(q: list[list[Fraction]], x: list[Fraction]) -> Fraction:
    return dot(x, matvec(q, x))


def main() -> None:
    for path, expected in EXPECTED_BLOBS.items():
        req(path.is_file(), f"missing source lock: {path.relative_to(ROOT)}")
        req(blob(path) == expected, f"source-lock drift: {path.relative_to(ROOT)}")

    cert = json.loads(CERT.read_text())
    stored = cert.pop("canonical_sha256_without_this_field", None)
    req(stored == EXPECTED_CERT_CANONICAL, "GRF-04 stored canonical drift")
    req(csha(cert) == EXPECTED_CERT_CANONICAL, "GRF-04 canonical drift")
    req(
        cert["status"]
        == "EXACT_SYMBOLIC_SCHUR_COMPLEMENT_LOWER_BOUND_KERNEL_NO_CONCRETE_178_TARGET_NO_CREDIT",
        "GRF-04 status drift",
    )

    grf01 = json.loads(GRF01.read_text())
    grf01_stored = grf01.pop("canonical_sha256_without_this_field", None)
    req(grf01_stored == EXPECTED_GRF01_CANONICAL, "GRF-01 stored canonical drift")
    req(csha(grf01) == EXPECTED_GRF01_CANONICAL, "GRF-01 canonical drift")
    req(
        any(x.startswith("RATIONAL_QUADRATIC_LOWER_BOUND_EMPTY:") for x in grf01["global_feasibility_region"]["emptiness_rules"]),
        "GRF-01 rational lower-bound contract missing",
    )

    design = GRF01_DESIGN.read_text()
    req("**C. Rational quadratic lower bound.**" in design, "GRF-01 step C missing")
    req("rho(u) = b(u)^T * (A Q^-1 A^T)^-1 * b(u)." in design, "GRF-01 Schur formula drift")
    req("178, not MAIN, must choose actual row/stratum/family parameters" in design, "GRF-01 ownership firewall drift")

    grf03 = json.loads(GRF03.read_text())
    grf03_stored = grf03.pop("canonical_sha256_without_this_field", None)
    req(grf03_stored == EXPECTED_GRF03_CANONICAL, "GRF-03 stored canonical drift")
    req(csha(grf03) == EXPECTED_GRF03_CANONICAL, "GRF-03 canonical drift")
    req(
        "must use norm magnitude/bounds" in grf03["consequence"]["interpretation"],
        "GRF-03 next-route statement drift",
    )

    f1 = schur_minimum([[2, 0], [0, 3]], [[1, 1]], [1])
    req(f1["rho"] == Fraction(6, 5), "fixture1 rho drift")
    req(f1["v_star"] == [Fraction(3, 5), Fraction(2, 5)], "fixture1 minimizer drift")

    f2 = schur_minimum([[2, 0], [0, 3]], [[1, 1], [2, 2]], [1, 2])
    req(f2["rho"] == f1["rho"] and f2["v_star"] == f1["v_star"], "redundant-row invariance drift")

    f3 = schur_minimum([[2, 0], [0, 3]], [[1, 1], [2, 2]], [1, 3])
    req(f3["status"] == "LINEAR_CONSTRAINT_EMPTY", "inconsistent affine system did not fail closed")

    f4 = schur_minimum([[2, 1], [1, 2]], [[1, -1]], [1])
    req(f4["rho"] == Fraction(1, 2), "fixture4 rho drift")
    req(f4["v_star"] == [Fraction(1, 2), Fraction(-1, 2)], "fixture4 minimizer drift")

    q = qmatrix([[2, 0], [0, 3]])
    v = [Fraction(1), Fraction(0)]
    vs = f1["v_star"]
    delta = [v[i] - vs[i] for i in range(2)]
    req(qnorm(q, v) == f1["rho"] + qnorm(q, delta), "orthogonal decomposition drift")

    f5 = schur_minimum([[2, 1], [1, 2]], [], [])
    req(f5["rho"] == 0 and f5["v_star"] == [0, 0], "empty-constraint minimum drift")

    sem = cert["fail_closed_semantics"]
    req(sem["q_must_be_symmetric_positive_definite"], "SPD firewall drift")
    req(sem["inconsistent_affine_system_is_linear_empty"], "linear-empty firewall drift")
    req(sem["redundant_constraints_must_not_change_rho"], "redundancy firewall drift")
    req(sem["strict_inequality_required_for_quadratic_lower_bound_empty"], "strict inequality firewall drift")
    req(not sem["rho_leq_bound_proves_existence"], "existence overclaim")
    req(not sem["rational_feasibility_proves_integral_feasibility"], "integrality overclaim")
    req(not cert["ownership"]["concrete_row_or_stratum_selected"], "MAIN selected a concrete 178 target")
    req(not cert["ownership"]["population_replay_performed"], "MAIN replayed FULL178 population")
    req(not cert["credit_firewall"]["main_pruning_credit"], "unexpected MAIN pruning credit")
    req(not cert["credit_firewall"]["full178_complete"], "unexpected FULL178 completion")
    req(not cert["credit_firewall"]["merge_authorized"], "unexpected merge authorization")

    print("GRF-04 PASS: exact Schur-complement rational lower-bound kernel frozen; no concrete FULL178 target and no credit.")


if __name__ == "__main__":
    main()
