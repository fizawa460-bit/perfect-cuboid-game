#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages/stage36/36-09AQ/odd-eta-plus-monsky-class-coordinate-adapter-preflight.json"
AP = ROOT / "stages/stage36/36-09AP/retained-open-tunnell-monsky-two-gate-preflight.json"
AP_SOURCE = ROOT / "stages/stage36/36-09AP/retained-open-tunnell-monsky-two-gate-source-lock.md"
AO_SOURCE = ROOT / "stages/stage36/36-09AO/monsky-full2-kernel-source-lock.md"
MAIN_AM = ROOT / "stages/stage36/36-09AM/uniform-rankzero-tunnell-sha2-sieve-preflight.json"
STATE = ROOT / "stages/stage36/MAIN-STATE.json"

BASE = "ab8fd6b3ff6660188d7d17c89960f02f5bf9eb90"
AP_HEAD = "ce04f0158633f4fa935fb0949238d5b8d0ce10a2"
AP_CI = "34080266302/101614090384"
CERT_BLOB = "ac75db896e04664c50c26399b5f8af333e38cca1"
AP_BLOB = "354b2922cb633518c6cf7b47e7afb216481d2968"
AP_SOURCE_BLOB = "7fceb4a822cae8b7e33401919733cbe81677b730"
AO_SOURCE_BLOB = "9f22dfe19d42d7104d30d219aac1cfd72a67c72a"
MAIN_AM_BLOB = "6d9e9392df8fc70a90a356932724e0a589b6b446"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def sf(n: int) -> int:
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


def eta_plus_rep(A: int, B: int, C: int, D: int, t: int) -> tuple[list[int], list[int], list[int]]:
    N = A * B * C * D
    if t == 0:
        stage = [C * D, A * D, A * C]
        reordered = [stage[1], stage[2], stage[0]]
        torsion = [1, 1, 1]
        expected = [A * D, A * C, C * D]
    else:
        stage = [C * D, 2 * A * D, 2 * A * C]
        reordered = [stage[1], stage[2], stage[0]]
        torsion = [2, 2 * N, N]
        expected = [A * D, B * D, A * B]
    rep = [sf(x * y) for x, y in zip(reordered, torsion)]
    assert rep == expected
    return stage, reordered, rep


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
    assert blob(AP) == AP_BLOB
    assert blob(AP_SOURCE) == AP_SOURCE_BLOB
    assert blob(AO_SOURCE) == AO_SOURCE_BLOB
    assert blob(MAIN_AM) == MAIN_AM_BLOB
    subprocess.check_call(["git", "merge-base", "--is-ancestor", BASE, "HEAD"], cwd=ROOT)
    subprocess.check_call(["git", "merge-base", "--is-ancestor", AP_HEAD, "HEAD"], cwd=ROOT)
    assert git("rev-parse", f"{AP_HEAD}:stages/stage36/36-09AP/retained-open-tunnell-monsky-two-gate-preflight.json") == AP_BLOB

    c = json.loads(CERT.read_text())
    assert c["schema"] == "STAGE36_36_09AQ_ODD_ETA_PLUS_MONSKY_CLASS_COORDINATE_ADAPTER_PREFLIGHT_V1"
    assert c["base_main_sha"] == BASE
    bp = c["batch_parent"]
    assert bp["pr"] == 1680
    assert bp["36_09AP_exact_head"] == AP_HEAD
    assert bp["36_09AP_exact_head_ci"] == AP_CI

    h = c["hypotheses"]
    assert h["eta"] == "+1"
    assert h["consequence"] == "e=f=t with t in {0,1}"
    assert h["stage36_root_order"] == ["0", "+N", "-N"]
    assert h["monsky_root_order"] == ["+N", "-N", "0"]

    t0, t1 = c["t0"], c["t1"]
    assert t0["positive_divisor_representative"] == ["A*D", "A*C", "C*D"]
    assert t0["kernel_vector_formula"] == "(psi_N(A*C) | psi_N(A*D))"
    assert t1["positive_divisor_representative"] == ["A*D", "B*D", "A*B"]
    assert t1["kernel_vector_formula"] == "(psi_N(B*D) | psi_N(A*D))"

    samples = [(5, 7, 11, 13), (17, 19, 23, 29), (1, 7, 11, 13)]
    for A, B, C, D in samples:
        vals = [A, B, C, D]
        for i in range(4):
            for j in range(i + 1, 4):
                assert math.gcd(vals[i], vals[j]) == 1
        N = A * B * C * D
        for t in (0, 1):
            stage, reordered, rep = eta_plus_rep(A, B, C, D, t)
            assert all(x > 0 for x in stage)
            assert all(d > 0 and N % d == 0 for d in rep)
            assert sf(rep[0] * rep[1] * rep[2]) == 1
            if t == 0:
                assert reordered == [A * D, A * C, C * D]
                assert rep == [A * D, A * C, C * D]
            else:
                assert reordered == [2 * A * D, 2 * A * C, C * D]
                assert rep == [A * D, B * D, A * B]

    A, B, C, D = 5, 7, 11, 13
    primes = [5, 7, 11, 13]
    _, _, rep0 = eta_plus_rep(A, B, C, D, 0)
    _, _, rep1 = eta_plus_rep(A, B, C, D, 1)
    v0 = psi(rep0[1], primes) + psi(rep0[0], primes)
    v1 = psi(rep1[1], primes) + psi(rep1[0], primes)
    assert v0 == psi(A * C, primes) + psi(A * D, primes)
    assert v1 == psi(B * D, primes) + psi(A * D, primes)

    ap = json.loads(AP.read_text())
    assert ap["interpretation"]["odd_eta_minus_adapter_complete"] is True
    assert ap["retained_receiver_two_gate_implication"]["receiver_implies_both"] is True
    assert ap["retained_receiver_two_gate_implication"]["converse_from_both_gates_to_receiver"] is False

    cs = c["completion_status"]
    assert cs["odd_eta_minus_adapter"] == "COMPLETE_IN_36_09AP"
    assert cs["odd_eta_plus_adapter"] == "COMPLETE_IN_36_09AQ"
    assert cs["odd_N_all_eta_signs_adapter_complete"] is True
    assert cs["even_N_adapter_complete"] is False
    assert cs["retained_receiver_two_gate_filter_converse"] is False
    assert cs["candidate_parameter_set_shrunk"] is False
    assert cs["receiver_closed"] is False

    st = json.loads(STATE.read_text())
    assert st["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V79_36_09AQ_CANDIDATE"
    assert st["base_main_sha"] == BASE
    aq = st["authority_frontier"]["36-09AQ"]
    assert aq["ODD_ETA_PLUS_MONSKY_COORDINATE_ADAPTER"] is True
    assert aq["ODD_N_ALL_ETA_MONSKY_COORDINATE_ADAPTER"] is True
    assert aq["EVEN_MONSKY_COORDINATE_ADAPTER"] is False
    assert aq["RECEIVER_CLOSED"] is False
    assert st["current"]["unit"] == "36-09AR"
    assert st["current"]["36_09AR_entry_allowed"] is True
    assert st["claims"]["candidate_parameter_set_shrunk"] is False
    assert st["claims"]["receiver_emptiness_proved"] is False

    print("36-09AQ verified: odd eta-plus Stage36 full-2 classes torsion-normalize exactly into Monsky positive-divisor representatives for t=0,1; combined with AP, all odd-N eta signs are adapted; no Monsky converse, parameter shrink, or receiver closure; AR unlocked")


if __name__ == "__main__":
    main()
