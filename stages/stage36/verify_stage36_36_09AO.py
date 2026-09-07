#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages/stage36/36-09AO/monsky-stage36-full2-class-adapter-preflight.json"
SOURCE = ROOT / "stages/stage36/36-09AO/monsky-full2-kernel-source-lock.md"
AN = ROOT / "stages/stage36/36-09AN/tunnell-filter-residue-noncompression-preflight.json"
AL = ROOT / "stages/stage36/36-09AL/b7-selmer-class-nontrivial-sha2-preflight.json"
PW07 = ROOT / "docs/arsenal/cards/provisional/S36-PW07.md"
STATE = ROOT / "stages/stage36/MAIN-STATE.json"

BASE = "24215fa27a631cd3cb370c0dfd76866dd2e916f1"
AN_HEAD = "8ade3e831595143280cee1bf39fb94205075e2cd"
AN_CI = "34076840101/101604523353"
CERT_BLOB = "a26991cb071e086d3cbc36b8c9d2db329a14e5b1"
SOURCE_BLOB = "9f22dfe19d42d7104d30d219aac1cfd72a67c72a"
AN_BLOB = "7bc094390cd4d82d9dee6959eb934185c8c4c492"
AN_VERIFIER_BLOB = "pending"
AL_BLOB = "10962f8d2471a8236d66a602c0f4952ce497e56c"
PW07_BLOB = "9ebeb753826da005471bf677969b535f91ea8018"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def sf(n: int) -> int:
    assert n != 0
    sign = -1 if n < 0 else 1
    n = abs(n)
    out = 1
    p = 2
    while p * p <= n:
        parity = 0
        while n % p == 0:
            n //= p
            parity ^= 1
        if parity:
            out *= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out *= n
    return sign * out


def additive_legendre(a: int, p: int) -> int:
    r = pow(a % p, (p - 1) // 2, p)
    assert r in (1, p - 1)
    return 0 if r == 1 else 1


def add(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    return [[x ^ y for x, y in zip(rx, ry)] for rx, ry in zip(A, B)]


def diag(vals: list[int]) -> list[list[int]]:
    n = len(vals)
    return [[vals[i] if i == j else 0 for j in range(n)] for i in range(n)]


def monskey_odd(primes: list[int]) -> tuple[list[list[int]], list[int], list[int], list[list[int]]]:
    k = len(primes)
    A = [[0] * k for _ in range(k)]
    for i, p in enumerate(primes):
        for j, q in enumerate(primes):
            if i != j:
                A[i][j] = additive_legendre(q, p)
        A[i][i] = sum(A[i][j] for j in range(k) if j != i) & 1
    d2v = [additive_legendre(2, p) for p in primes]
    dm2v = [additive_legendre(-2, p) for p in primes]
    D2 = diag(d2v)
    Dm2 = diag(dm2v)
    TL = add(A, D2)
    BR = add(A, Dm2)
    M = [TL[i] + D2[i] for i in range(k)] + [D2[i] + BR[i] for i in range(k)]
    return A, d2v, dm2v, M


def rank_f2(M: list[list[int]]) -> int:
    a = [row[:] for row in M]
    nr, nc = len(a), len(a[0])
    r = 0
    for c in range(nc):
        piv = next((i for i in range(r, nr) if a[i][c]), None)
        if piv is None:
            continue
        a[r], a[piv] = a[piv], a[r]
        for i in range(nr):
            if i != r and a[i][c]:
                a[i] = [x ^ y for x, y in zip(a[i], a[r])]
        r += 1
    return r


def matvec(M: list[list[int]], v: list[int]) -> list[int]:
    return [sum(x * y for x, y in zip(row, v)) & 1 for row in M]


def psi(d: int, primes: list[int]) -> list[int]:
    assert d > 0
    out = []
    for p in primes:
        e = 0
        while d % p == 0:
            d //= p
            e ^= 1
        out.append(e)
    assert d == 1
    return out


def main() -> None:
    assert blob(CERT) == CERT_BLOB
    assert blob(SOURCE) == SOURCE_BLOB
    assert blob(AN) == AN_BLOB
    assert blob(AL) == AL_BLOB
    assert blob(PW07) == PW07_BLOB
    subprocess.check_call(["git", "merge-base", "--is-ancestor", BASE, "HEAD"], cwd=ROOT)
    subprocess.check_call(["git", "merge-base", "--is-ancestor", AN_HEAD, "HEAD"], cwd=ROOT)
    assert git("rev-parse", f"{AN_HEAD}:stages/stage36/36-09AN/tunnell-filter-residue-noncompression-preflight.json") == AN_BLOB

    c = json.loads(CERT.read_text())
    assert c["schema"] == "STAGE36_36_09AO_MONSKY_STAGE36_FULL2_CLASS_ADAPTER_PREFLIGHT_V1"
    assert c["base_main_sha"] == BASE
    bp = c["batch_parent"]
    assert bp["pr"] == 1680
    assert bp["36_09AN_exact_head"] == AN_HEAD
    assert bp["36_09AN_exact_head_ci"] == AN_CI

    ga = c["general_adapter"]
    assert ga["stage36_root_order"] == ["0", "+N", "-N"]
    assert ga["monsky_homogeneous_root_order"] == ["+N", "-N", "0"]
    assert ga["odd_N_kernel_map"] == "(d1,d2,d3) -> (psi_N(d2),psi_N(d1))"

    # Exact B7 representative normalization in the pure Selmer quotient.
    b = c["B7_exact_adapter"]
    n = b["N"]
    primes = b["prime_order"]
    assert n == 73073 == 7 * 11 * 13 * 73
    assert primes == [7, 11, 13, 73]
    stage = b["stage36_normalized_triple_0_plus_minus"]
    assert stage == [-143, -1606, 1898]
    reordered = [stage[1], stage[2], stage[0]]
    assert reordered == b["monsky_reordered_triple_plus_minus_0"] == [-1606, 1898, -143]
    torsion = [-2 * n, 2, -n]
    standard = [sf(x * y) for x, y in zip(reordered, torsion)]
    assert standard == b["positive_divisor_representative"] == [91, 949, 511]
    assert all(d > 0 and n % d == 0 for d in standard)
    assert sf(standard[0] * standard[1] * standard[2]) == 1
    p_d2 = psi(standard[1], primes)
    p_d1 = psi(standard[0], primes)
    v = p_d2 + p_d1
    assert p_d2 == b["psi_d2"] == [0, 0, 1, 1]
    assert p_d1 == b["psi_d1"] == [1, 0, 1, 0]
    assert v == b["kernel_vector"] == [0, 0, 1, 1, 1, 0, 1, 0]

    A, d2, dm2, M = monskey_odd(primes)
    assert A == b["A_matrix"]
    assert d2 == b["D2_diag"]
    assert dm2 == b["Dminus2_diag"]
    assert M == b["Monsky_matrix"]
    assert matvec(M, v) == b["M_times_kernel_vector"] == [0] * 8
    rk = rank_f2(M)
    null = len(M) - rk
    assert (rk, null) == (b["matrix_rank_F2"], b["matrix_nullity"]) == (6, 2)
    assert b["pure_2Selmer_dimension"] == null

    # Audited AL rank-zero/no-4-torsion makes pure MW dimension zero, so
    # the pure Selmer nullity equals dim Sha[2] for this fixed fiber.
    al = json.loads(AL.read_text())
    assert al["tunnell_exact_enumeration"]["Mordell_Weil_rank_E73073"] == 0
    assert al["Mordell_Weil_mod2_Kummer_image"]["rational_4torsion_absent"] is True
    assert al["Selmer_to_Sha_conclusion"]["covering_class_maps_to_nonzero_Sha2"] is True
    assert b["audited_AL_MW_rank"] == 0
    assert b["audited_AL_no_rational_4torsion"] is True
    assert b["Sha2_dimension_F2"] == null == 2
    assert b["Sha2_order"] == 2 ** null == 4
    assert any(v)
    assert b["Stage36_class_is_nonzero_kernel_vector"] is True

    # B23 is a matrix diagnostic only.
    b23 = c["B23_matrix_diagnostic"]
    p23 = b23["prime_order"]
    assert p23 == [11, 13, 23, 73]
    assert b23["N"] == 240097 == 11 * 13 * 23 * 73
    _, _, _, M23 = monskey_odd(p23)
    r23 = rank_f2(M23)
    assert (r23, len(M23) - r23) == (6, 2)
    assert b23["matrix_rank_F2"] == 6 and b23["matrix_nullity"] == 2
    assert b23["Stage36_class_local_survivor_claimed"] is False
    assert b23["rank_or_congruence_claimed"] is False

    rr = c["route_result"]
    assert rr["MONSKY_MATRIX_CONSTRUCTION_ADAPTED"] is True
    assert rr["STAGE36_FULL2_CLASS_TO_KERNEL_ADAPTED_FOR_ODD_B7"] is True
    assert rr["EVEN_STAGE36_CLASS_EXAMPLE_ADAPTED"] is False
    assert rr["UNIFORM_MW_VS_SHA_CLASSIFIED"] is False
    assert rr["natural_hostile_audit_checkpoint"] is True

    st = json.loads(STATE.read_text())
    assert st["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V77_36_09AO_BATCH_AUDIT_CHECKPOINT"
    ao = st["authority_frontier"]["36-09AO"]
    assert ao["MONSKY_MATRIX_CONSTRUCTION_ADAPTED"] is True
    assert ao["B7_KERNEL_VECTOR"] == v
    assert ao["B7_MONSKY_NULLITY"] == 2
    assert ao["B7_SHA2_DIMENSION"] == 2
    assert ao["UNIFORM_MW_VS_SHA_CLASSIFIED"] is False
    assert st["current"]["unit"] == "36-09AO-AUDIT-CHECKPOINT"
    assert st["current"]["next_owner"] == "HOSTILE_AUDIT"
    assert st["current"]["36_09AP_entry_allowed"] is False
    assert st["claims"]["candidate_parameter_set_shrunk"] is False
    assert st["claims"]["receiver_emptiness_proved"] is False

    print("36-09AO verified: actual-prime Monsky matrix adapter exact; B7 Stage36 class torsion-normalizes to (91,949,511) and kernel vector (0011|1010); rank=6/nullity=2, hence audited rank-zero fiber has Sha[2] dimension 2; even branch execution and uniform MW/Sha classification remain open; AP locked at hostile-audit checkpoint")


if __name__ == "__main__":
    main()
