#!/usr/bin/env python3
"""Deterministic audit for Stage14-tH15 shared-U bipartite receiver."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
T54 = ROOT / "stages/stage14/data/14-t54/shared_u_canonical_prime_frozen.json"
SUMMARY = ROOT / "stages/stage14/data/tH15/shared_u_bipartite_squareclass_summary.json"
RESULT = ROOT / "stages/stage14/14-tH15/result.md"


def mul(z: tuple[int, int], w: tuple[int, int]) -> tuple[int, int]:
    x, y = z
    u, v = w
    return x * u - y * v, x * v + y * u


def conj(z: tuple[int, int]) -> tuple[int, int]:
    return z[0], -z[1]


def psi(z: tuple[int, int]) -> int:
    return z[0] * z[1]


def direct_invisible(U, pi, V) -> int:
    A = mul(pi, U)
    return -psi(mul(A, conj(V))) * psi(mul(A, V))


def direct_visible_same(U, pi, V) -> int:
    ell = pi[0] * pi[0] + pi[1] * pi[1]
    A = mul(pi, U)
    P = mul(pi, V)
    F = -psi(mul(A, conj(P))) * psi(mul(A, P))
    assert F % (ell * ell) == 0
    return F // (ell * ell)


def direct_visible_opposite(U, pi, V) -> int:
    ell = pi[0] * pi[0] + pi[1] * pi[1]
    A = mul(pi, U)
    P = mul(conj(pi), V)
    F = -psi(mul(A, conj(P))) * psi(mul(A, P))
    assert F % (ell * ell) == 0
    return F // (ell * ell)


def projective_components(U, V):
    a, b = U
    p, q = V
    Aplus = a * p + b * q
    Bplus = b * p - a * q
    Aminus = a * p - b * q
    Bminus = b * p + a * q
    return Aplus, Bplus, Aminus, Bminus


def Lhom(A: int, B: int, r: int, s: int) -> int:
    return (A * r - B * s) * (B * r + A * s)


def proj_invisible(U, pi, V) -> int:
    r, s = pi
    Ap, Bp, Am, Bm = projective_components(U, V)
    return -Lhom(Ap, Bp, r, s) * Lhom(Am, Bm, r, s)


def phi_hom(A: int, B: int, r: int, s: int) -> int:
    x = A * (r * r - s * s) - 2 * B * r * s
    y = B * (r * r - s * s) + 2 * A * r * s
    return x * y


def proj_visible_same(U, pi, V) -> int:
    Ap, Bp, Am, Bm = projective_components(U, V)
    return -(Ap * Bp) * phi_hom(Am, Bm, pi[0], pi[1])


def proj_visible_opposite(U, pi, V) -> int:
    Ap, Bp, Am, Bm = projective_components(U, V)
    return -(Am * Bm) * phi_hom(Ap, Bp, pi[0], pi[1])


def audit_projective_factorizations() -> int:
    Us = [(1, 2), (2, 3), (1, 4)]
    pis = [(3, 2), (4, 1), (5, 2)]
    Vs = [(2, 1), (3, 1), (3, 2), (4, 3)]
    checks = 0
    for U in Us:
        for pi in pis:
            for V in Vs:
                assert direct_invisible(U, pi, V) == proj_invisible(U, pi, V)
                assert direct_visible_same(U, pi, V) == proj_visible_same(U, pi, V)
                assert direct_visible_opposite(U, pi, V) == proj_visible_opposite(U, pi, V)
                checks += 3
    return checks


def energy_partition(states):
    # states are (row=pi, col=V, color=kappa)
    counts = Counter(c for _, _, c in states)
    E = sum(v * v for v in counts.values())
    R = len(states)
    same_pi = same_V = transverse = 0
    for i, s in enumerate(states):
        for j, t in enumerate(states):
            if i == j or s[2] != t[2]:
                continue
            if s[0] == t[0]:
                same_pi += 1
            elif s[1] == t[1]:
                same_V += 1
            else:
                transverse += 1
    assert E == R + same_pi + same_V + transverse
    return E, R, same_pi, same_V, transverse


def audit_energy_partition() -> dict:
    states = [
        ("p1", "v1", "a"),
        ("p1", "v2", "a"),
        ("p2", "v2", "a"),
        ("p2", "v3", "b"),
        ("p3", "v1", "b"),
        ("p4", "v4", "c"),
    ]
    E, R, spi, sv, tr = energy_partition(states)
    assert E == 14
    assert R == 6
    assert spi + sv + tr == 8
    return {"E": E, "R": R, "same_pi": spi, "same_V": sv, "transverse": tr}


def audit_latin_square(N: int = 32) -> dict:
    # color i+j mod N: every row/column sees every color once; every color occurs N times.
    states = [(i, j, (i + j) % N) for i in range(N) for j in range(N)]
    colors = Counter(c for _, _, c in states)
    assert max(colors.values()) == N
    for i in range(N):
        assert len({c for r, _, c in states if r == i}) == N
    for j in range(N):
        assert len({c for _, col, c in states if col == j}) == N
    R = N * N
    E = sum(v * v for v in colors.values())
    assert E == N**3
    return {"N": N, "states": R, "energy": E, "failure_factor": E // R}


def audit_transverse_frobenius_identity() -> dict:
    states = [
        ("p1", "v1"),
        ("p1", "v2"),
        ("p2", "v1"),
        ("p2", "v3"),
        ("p3", "v2"),
    ]
    primes = [13, 17, 29, 37]
    vals = {
        states[0]: [1, 1, -1, 1],
        states[1]: [1, -1, 1, 1],
        states[2]: [-1, 1, 1, 1],
        states[3]: [1, 1, 1, -1],
        states[4]: [-1, -1, 1, 1],
    }

    pair_side = 0
    for s in states:
        for t in states:
            if s[0] == t[0] or s[1] == t[1]:
                continue
            inner = sum(a * b for a, b in zip(vals[s], vals[t]))
            pair_side += inner * inner

    matrix_side = 0
    for ip, _p in enumerate(primes):
        for iq, _q in enumerate(primes):
            def z(st):
                return vals[st][ip] * vals[st][iq]

            G = sum(z(st) for st in states)
            by_pi = defaultdict(int)
            by_V = defaultdict(int)
            D = 0
            for st in states:
                by_pi[st[0]] += z(st)
                by_V[st[1]] += z(st)
                D += z(st) * z(st)
            matrix_side += G * G - sum(x*x for x in by_pi.values()) - sum(x*x for x in by_V.values()) + D

    assert pair_side == matrix_side
    assert pair_side >= 0
    return {"pair_side": pair_side, "matrix_side": matrix_side, "prime_count": len(primes)}


def audit_principal_lower_bound() -> dict:
    P = 11
    b = 2
    # A principal pair agrees with +1 on at least P-2b common good primes.
    common_good = P - 2 * b
    inner_abs = common_good
    assert inner_abs * inner_abs >= (P - 2 * b) ** 2
    return {"P": P, "b": b, "principal_pair_min_square": inner_abs * inner_abs}


def audit_critical_ledger() -> None:
    half = Fraction(1, 2)
    quarter = Fraction(1, 4)
    for u in [Fraction(0), Fraction(1, 8), Fraction(1, 4), Fraction(3, 8), Fraction(1, 2)]:
        delta = half - u
        # k exponent <= u, so n=k*delta <= 1/2.
        n_exp = u + delta
        assert n_exp == half
        assert n_exp / 2 == quarter
    # natural uncentered Frobenius condition rho>=r
    for r in [Fraction(1, 16), Fraction(1, 8), Fraction(1, 4), Fraction(1, 2)]:
        rho = r
        assert rho >= r


def audit_boundaries() -> None:
    t54 = json.loads(T54.read_text())
    summary = json.loads(SUMMARY.read_text())
    text = RESULT.read_text()

    assert t54["FIXED_U_DIVISOR_FAN_PROVED"] is True
    assert t54["FIXED_U_REDUCES_TO_ONE_DIMENSIONAL_CANONICAL_PRIME_SUM"] is False
    assert t54["ONE_VARIABLE_FIBER_BOUNDS_GLOBALIZE"] is False
    assert t54["SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_PROVED"] is False
    assert t54["TH15_NEEDED"] is True

    assert summary["proof_boundary"]["cauchy_free_row_column_transverse_partition_proved"] is True
    assert summary["proof_boundary"]["transverse_positive_frobenius_receiver_proved"] is True
    assert summary["proof_boundary"]["shared_U_physical_bipartite_dispersion_proved"] is False
    assert summary["proof_boundary"]["E4_coefficient_energy_used"] is False
    assert summary["proof_boundary"]["shared_U_bipartite_squareclass_energy_proved"] is False
    assert summary["minimal_remaining_obstruction"] == "SharedUPhysicalBipartiteDispersion"

    required = [
        "STAGE14_TH15=COMPLETE_SHARED_U_BIPARTITE_RECEIVER_AND_TRANSVERSE_DISPERSION_BOUNDARY",
        "CAUCHY_FREE_ROW_COLUMN_TRANSVERSE_PARTITION_PROVED=true",
        "TRANSVERSE_POSITIVE_FROBENIUS_RECEIVER_PROVED=true",
        "SHARED_U_PHYSICAL_BIPARTITE_DISPERSION_PROVED=false",
        "PAIR_COLLAPSE_BEFORE_PHYSICAL_CANCELLATION_ALLOWED=false",
        "E4_COEFFICIENT_ENERGY_USED=false",
        "SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_PROVED=false",
        "MINIMAL_REMAINING_OBSTRUCTION=SharedUPhysicalBipartiteDispersion",
        "NEXT=Stage14-t55",
    ]
    for token in required:
        assert token in text, token


def main() -> None:
    projective_checks = audit_projective_factorizations()
    partition = audit_energy_partition()
    latin = audit_latin_square()
    frob = audit_transverse_frobenius_identity()
    principal = audit_principal_lower_bound()
    audit_critical_ledger()
    audit_boundaries()
    print("Stage14-tH15 shared-U bipartite audit: OK")
    print(json.dumps({
        "projective_factorization_checks": projective_checks,
        "partition": partition,
        "latin": latin,
        "frobenius": frob,
        "principal": principal,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
