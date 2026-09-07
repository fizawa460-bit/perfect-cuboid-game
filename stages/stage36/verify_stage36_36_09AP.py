#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages/stage36/36-09AP/retained-open-tunnell-monsky-two-gate-preflight.json"
SOURCE = ROOT / "stages/stage36/36-09AP/retained-open-tunnell-monsky-two-gate-source-lock.md"
MAIN_AN = ROOT / "stages/stage36/36-09AN/retained-open-tunnell-necessary-gate-preflight.json"
MAIN_AN_SOURCE = ROOT / "stages/stage36/36-09AN/retained-open-congruent-number-rank-gate-source-lock.md"
AO = ROOT / "stages/stage36/36-09AO/monsky-stage36-full2-class-adapter-preflight.json"
AO_SOURCE = ROOT / "stages/stage36/36-09AO/monsky-full2-kernel-source-lock.md"
OLD_AN = ROOT / "stages/stage36/36-09AN/tunnell-filter-residue-noncompression-preflight.json"
STATE = ROOT / "stages/stage36/MAIN-STATE.json"

BASE = "6b6c541d1a6bbe229381ac0400148bd17523ca06"
PR1679_HEAD = "12716259951f02589ecfaf6ac8f9670b7a23f06f"
PR1679_AUDIT = 5127771308
PR1679_CI = "34076440104/101603376687"
PR1680_AUDITED_HEAD = "f5db4fc0aafdc61f931b6499afb18c1966c1f99d"
PR1680_AUDIT = 5127677576
PR1680_CI = "34077287921/101605797971"
RECONCILE = "7c0059ccfd67dbf939a36b083fe3ba70d64a42b5"

CERT_BLOB = "354b2922cb633518c6cf7b47e7afb216481d2968"
SOURCE_BLOB = "7fceb4a822cae8b7e33401919733cbe81677b730"
MAIN_AN_BLOB = "76c55e89505b081c487749f4d7ab4d80e9d38a1f"
MAIN_AN_SOURCE_BLOB = "1486507569cd9b6263ff46c5db263fbbc198e87c"
AO_BLOB = "a26991cb071e086d3cbc36b8c9d2db329a14e5b1"
AO_SOURCE_BLOB = "9f22dfe19d42d7104d30d219aac1cfd72a67c72a"
OLD_AN_BLOB = "7bc094390cd4d82d9dee6959eb934185c8c4c492"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def additive_legendre(a: int, p: int) -> int:
    r = pow(a % p, (p - 1) // 2, p)
    assert r in (1, p - 1)
    return 0 if r == 1 else 1


def diag(vals: list[int]) -> list[list[int]]:
    n = len(vals)
    return [[vals[i] if i == j else 0 for j in range(n)] for i in range(n)]


def madd(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
    return [[x ^ y for x, y in zip(ar, br)] for ar, br in zip(A, B)]


def monsky_odd(primes: list[int]) -> list[list[int]]:
    k = len(primes)
    A = [[0] * k for _ in range(k)]
    for i, p in enumerate(primes):
        for j, q in enumerate(primes):
            if i != j:
                A[i][j] = additive_legendre(q, p)
        A[i][i] = sum(A[i][j] for j in range(k) if j != i) & 1
    d2 = [additive_legendre(2, p) for p in primes]
    dm2 = [additive_legendre(-2, p) for p in primes]
    D2, Dm2 = diag(d2), diag(dm2)
    TL, BR = madd(A, D2), madd(A, Dm2)
    return [TL[i] + D2[i] for i in range(k)] + [D2[i] + BR[i] for i in range(k)]


def matvec(M: list[list[int]], v: list[int]) -> list[int]:
    return [sum(a * b for a, b in zip(row, v)) & 1 for row in M]


def rank_f2(M: list[list[int]]) -> int:
    a = [r[:] for r in M]
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


def psi(d: int, primes: list[int]) -> list[int]:
    assert d > 0
    out: list[int] = []
    for p in primes:
        e = 0
        while d % p == 0:
            d //= p
            e ^= 1
        out.append(e)
    assert d == 1
    return out


def squarefree(n: int) -> int:
    sign = -1 if n < 0 else 1
    n = abs(n)
    out = 1
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e ^= 1
        if e:
            out *= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out *= n
    return sign * out


def tunnell_parity_counts(n: int) -> tuple[int, int]:
    assert n > 0
    a = 1 if n & 1 else 2
    m = n // a
    even = odd = 0
    xmax = math.isqrt(m // (2 * a)) if m >= 2 * a else 0
    zmax = math.isqrt(m // 8)
    for x in range(-xmax, xmax + 1):
        remx = m - 2 * a * x * x
        if remx < 0:
            continue
        for z in range(-zmax, zmax + 1):
            rem = remx - 8 * z * z
            if rem < 0:
                continue
            y = math.isqrt(rem)
            if y * y == rem:
                mult = 1 if y == 0 else 2
                if z & 1:
                    odd += mult
                else:
                    even += mult
    return even, odd


def eta_minus_rep(A: int, B: int, C: int, D: int, t: int) -> tuple[list[int], list[int]]:
    N = A * B * C * D
    if t == 0:
        stage = [-C * D, -A * C, A * D]
        reordered = [stage[1], stage[2], stage[0]]
        torsion = [-N, N, -1]
        expected = [B * D, B * C, C * D]
    else:
        stage = [-C * D, -2 * A * C, 2 * A * D]
        reordered = [stage[1], stage[2], stage[0]]
        torsion = [-2 * N, 2, -N]
        expected = [B * D, A * D, A * B]
    rep = [squarefree(x * y) for x, y in zip(reordered, torsion)]
    assert rep == expected
    return stage, rep


def main() -> None:
    # Exact payload locks after reconciling two audited histories.
    assert blob(CERT) == CERT_BLOB
    assert blob(SOURCE) == SOURCE_BLOB
    assert blob(MAIN_AN) == MAIN_AN_BLOB
    assert blob(MAIN_AN_SOURCE) == MAIN_AN_SOURCE_BLOB
    assert blob(AO) == AO_BLOB
    assert blob(AO_SOURCE) == AO_SOURCE_BLOB
    assert blob(OLD_AN) == OLD_AN_BLOB
    subprocess.check_call(["git", "merge-base", "--is-ancestor", BASE, "HEAD"], cwd=ROOT)
    subprocess.check_call(["git", "merge-base", "--is-ancestor", PR1680_AUDITED_HEAD, "HEAD"], cwd=ROOT)
    subprocess.check_call(["git", "merge-base", "--is-ancestor", RECONCILE, "HEAD"], cwd=ROOT)
    assert git("rev-parse", f"{BASE}:stages/stage36/36-09AN/retained-open-tunnell-necessary-gate-preflight.json") == MAIN_AN_BLOB
    assert git("rev-parse", f"{PR1680_AUDITED_HEAD}:stages/stage36/36-09AO/monsky-stage36-full2-class-adapter-preflight.json") == AO_BLOB
    assert git("rev-parse", f"{PR1680_AUDITED_HEAD}:stages/stage36/36-09AO/monsky-full2-kernel-source-lock.md") == AO_SOURCE_BLOB

    c = json.loads(CERT.read_text())
    assert c["schema"] == "STAGE36_36_09AP_RETAINED_OPEN_TUNNELL_MONSKY_TWO_GATE_PREFLIGHT_V1"
    assert c["base_main_sha"] == BASE
    rc = c["reconciliation"]
    p79 = rc["current_main_stage36_parent"]
    assert p79["pr"] == 1679 and p79["post_merge_hostile_audit_review"] == PR1679_AUDIT
    assert p79["audited_exact_head"] == PR1679_HEAD and p79["exact_head_ci"] == PR1679_CI
    assert p79["squash_merged_main_sha"] == BASE
    p80 = rc["parallel_audited_monsky_payload"]
    assert p80["pr"] == 1680 and p80["hostile_audit_review"] == PR1680_AUDIT
    assert p80["audited_exact_head"] == PR1680_AUDITED_HEAD and p80["exact_head_ci"] == PR1680_CI
    assert rc["reconcile_merge_commit"] == RECONCILE

    main_an = json.loads(MAIN_AN.read_text())
    assert main_an["retained_open"]["normalized_image_avoids_all_rational_2torsion"] is True
    assert main_an["congruent_number_torsion_rank_gate"]["retained_receiver_implies_positive_MW_rank"] is True
    assert main_an["Tunnell_gate"]["retained_receiver_implies_parity_appropriate_Tunnell_equality"] is True
    assert main_an["Tunnell_gate"]["BSD_converse_used"] is False

    ao = json.loads(AO.read_text())
    assert ao["odd_matrix_convention"]["M_odd"] == "[[A+D2,D2],[D2,A+Dminus2]]"
    assert ao["general_adapter"]["odd_N_kernel_map"] == "(d1,d2,d3) -> (psi_N(d2),psi_N(d1))"

    gates = c["retained_receiver_two_gate_implication"]
    assert gates["receiver_implies_both"] is True
    assert gates["failure_of_either_excludes_branch"] is True
    assert gates["converse_from_both_gates_to_receiver"] is False
    assert gates["BSD_converse_used"] is False

    # Algebraic torsion normalizations for both odd eta=-1 parity cases.
    for vals in [(5, 7, 11, 13), (17, 19, 23, 29), (1, 7, 11, 13)]:
        A, B, C, D = vals
        N = A * B * C * D
        # pairwise coprime synthetic inputs only
        assert math.gcd(A * B, C * D) == math.gcd(A, B) == math.gcd(C, D) == 1
        for t in (0, 1):
            _, rep = eta_minus_rep(A, B, C, D, t)
            assert all(d > 0 and N % d == 0 for d in rep)
            assert squarefree(rep[0] * rep[1] * rep[2]) == 1

    # Exact B=7 replay.
    b7 = c["B7_exact_replay"]
    A, B, C, D = b7["A"], b7["B"], b7["C"], b7["D"]
    _, rep7 = eta_minus_rep(A, B, C, D, 1)
    assert rep7 == b7["positive_divisor_representative"] == [91, 949, 511]
    p7 = b7["prime_order"]
    v7 = psi(rep7[1], p7) + psi(rep7[0], p7)
    assert v7 == b7["kernel_vector"] == [0,0,1,1,1,0,1,0]
    M7 = monsky_odd(p7)
    assert matvec(M7, v7) == b7["Monsky_matrix_times_vector"] == [0] * 8
    r7 = rank_f2(M7)
    assert (r7, 8-r7) == (b7["Monsky_matrix_rank_F2"], b7["Monsky_matrix_nullity"]) == (6,2)
    e7, o7 = tunnell_parity_counts(b7["N"])
    assert (e7, o7) == (b7["Tunnell_N_even"], b7["Tunnell_N_odd"]) == (480,416)
    assert b7["Tunnell_gate_pass"] is False and b7["Monsky_gate_pass"] is True

    # Exact B=23 diagnostic: Tunnell passes but Stage36 class is outside Monsky kernel.
    b23 = c["B23_exact_diagnostic"]
    A, B, C, D = b23["A"], b23["B"], b23["C"], b23["D"]
    _, rep23 = eta_minus_rep(A, B, C, D, 1)
    assert rep23 == b23["positive_divisor_representative"] == [299,949,1679]
    p23 = b23["prime_order"]
    v23 = psi(rep23[1], p23) + psi(rep23[0], p23)
    assert v23 == b23["kernel_vector"] == [0,1,0,1,0,1,1,0]
    M23 = monsky_odd(p23)
    mv23 = matvec(M23, v23)
    assert mv23 == b23["Monsky_matrix_times_vector"] == [0,1,0,1,1,0,0,1]
    r23 = rank_f2(M23)
    assert (r23, 8-r23) == (6,2)
    e23, o23 = tunnell_parity_counts(b23["N"])
    assert (e23, o23) == (384,384)
    old_an = json.loads(OLD_AN.read_text())
    assert old_an["B23"]["Tunnell_equality"] is True
    assert old_an["B23"]["AF_selected_prime_rows_pass"] is False
    assert b23["Tunnell_gate_pass"] is True and b23["Monsky_gate_pass"] is False
    assert b23["local_or_receiver_survivor_claimed"] is False
    assert b23["congruent_or_positive_rank_claimed"] is False

    it = c["interpretation"]
    assert it["two_gates_logically_distinct_on_exact_same_parameter_diagnostic"] is True
    assert it["Monsky_kernel_membership_is_only_necessary"] is True
    assert it["Tunnell_equality_is_only_necessary"] is True
    assert it["odd_eta_minus_adapter_complete"] is True
    assert it["odd_eta_plus_adapter_complete"] is False
    assert it["even_N_adapter_complete"] is False
    assert it["candidate_parameter_set_shrunk"] is False and it["receiver_closed"] is False

    st = json.loads(STATE.read_text())
    assert st["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V78_36_09AP_RECONCILED_CANDIDATE"
    assert st["base_main_sha"] == BASE
    assert st["promotion_gates"]["36_09AM_AN_hostile_audit_passed"] is True
    assert st["promotion_gates"]["36_09AO_payload_hostile_audit_passed"] is True
    ap = st["authority_frontier"]["36-09AP"]
    assert ap["RETAINED_RECEIVER_TWO_GATE_FILTER"] is True
    assert ap["ODD_ETA_MINUS_MONSKY_COORDINATE_ADAPTER"] is True
    assert ap["ODD_ETA_PLUS_MONSKY_COORDINATE_ADAPTER"] is False
    assert ap["EVEN_MONSKY_COORDINATE_ADAPTER"] is False
    assert st["current"]["unit"] == "36-09AQ"
    assert st["current"]["36_09AQ_entry_allowed"] is True
    assert st["claims"]["candidate_parameter_set_shrunk"] is False
    assert st["claims"]["receiver_emptiness_proved"] is False
    assert st["claims"]["perfect_cuboid_nonexistence_claim"] is False

    print("36-09AP verified: audited #1679 retained-open Tunnell gate reconciled with audited #1680 Monsky payload; receiver implies both Tunnell equality and Stage36 Monsky-kernel membership; odd eta=-1 coordinate formulas exact; B7 fails Tunnell but passes Monsky, B23 passes Tunnell but fails Monsky; neither gate has a converse; AQ unlocked")


if __name__ == "__main__":
    main()
