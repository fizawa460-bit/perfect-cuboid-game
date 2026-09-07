#!/usr/bin/env python3
from __future__ import annotations

import json
import math
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages/stage36/36-09AR/even-monsky-class-coordinate-adapter-preflight.json"
AQ = ROOT / "stages/stage36/36-09AQ/odd-eta-plus-monsky-class-coordinate-adapter-preflight.json"
AQV = ROOT / "stages/stage36/verify_stage36_36_09AQ.py"
AO_SOURCE = ROOT / "stages/stage36/36-09AO/monsky-full2-kernel-source-lock.md"
AJ = ROOT / "stages/stage36/36-09AJ/congruent-number-full2-covering-class-preflight.json"
STATE = ROOT / "stages/stage36/MAIN-STATE.json"

BASE = "ab8fd6b3ff6660188d7d17c89960f02f5bf9eb90"
AQ_HEAD = "62497175353167faf98af7bfae6b6c2b3b32d013"
AQ_CI = "34082635055/101620706331"
CERT_BLOB = "667a2ab1329865acdefca3b531511a3798edb3e6"
AQ_BLOB = "ac75db896e04664c50c26399b5f8af333e38cca1"
AQV_BLOB = "235851de57165557d0aef4f59881561fe4e40c1a"
AO_SOURCE_BLOB = "9f22dfe19d42d7104d30d219aac1cfd72a67c72a"
AJ_BLOB = "27950f53a89e28d02d04f2c19628504561c206e7"


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


def psi(d: int, primes: list[int]) -> list[int]:
    d = abs(d)
    out = []
    for p in primes:
        e = 0
        while d % p == 0:
            d //= p
            e ^= 1
        out.append(e)
    assert d == 1
    return out


def branch(eta: int, e: int, f: int, A: int, B: int, C: int, D: int):
    assert eta in (-1, 1)
    assert (e, f) in ((0, 1), (1, 0))
    n = A * B * C * D
    N = 2 * n
    if eta == 1:
        stage = [2 * C * D, (2**f) * A * D, (2**e) * A * C]
    else:
        # AJ raw eta-minus class is normalized to positive N by swapping the two nonzero roots.
        stage = [-2 * C * D, -(2**e) * A * C, (2**f) * A * D]
    reordered = [stage[1], stage[2], stage[0]]

    if (eta, e, f) in ((1, 0, 1), (-1, 1, 0)):
        torsion = [2, 2 * N, N]          # (+N,0)
    else:
        torsion = [-2 * N, 2, -N]       # (-N,0)
    rep = [sf(x * y) for x, y in zip(reordered, torsion)]

    expected = {
        (1, 0, 1): [A * D, B * D, A * B],
        (1, 1, 0): [-B * C, A * C, -A * B],
        (-1, 0, 1): [B * D, A * D, A * B],
        (-1, 1, 0): [-A * C, B * C, -A * B],
    }[(eta, e, f)]
    assert rep == expected
    return stage, reordered, rep


def main() -> None:
    assert blob(CERT) == CERT_BLOB
    assert blob(AQ) == AQ_BLOB
    assert blob(AQV) == AQV_BLOB
    assert blob(AO_SOURCE) == AO_SOURCE_BLOB
    assert blob(AJ) == AJ_BLOB
    subprocess.check_call(["git", "merge-base", "--is-ancestor", BASE, "HEAD"], cwd=ROOT)
    subprocess.check_call(["git", "merge-base", "--is-ancestor", AQ_HEAD, "HEAD"], cwd=ROOT)
    assert git("rev-parse", f"{AQ_HEAD}:stages/stage36/36-09AQ/odd-eta-plus-monsky-class-coordinate-adapter-preflight.json") == AQ_BLOB

    c = json.loads(CERT.read_text())
    assert c["schema"] == "STAGE36_36_09AR_EVEN_MONSKY_CLASS_COORDINATE_ADAPTER_PREFLIGHT_V1"
    assert c["base_main_sha"] == BASE
    bp = c["batch_parent"]
    assert bp["36_09AQ_exact_head"] == AQ_HEAD
    assert bp["36_09AQ_exact_head_ci"] == AQ_CI
    h = c["hypotheses"]
    assert h["total_twist_N"] == "2*n"
    assert h["even_condition"] == "g=(e+f) mod 2=1, so (e,f) is (0,1) or (1,0)"
    assert h["stage36_root_order"] == ["0", "+N", "-N"]
    assert h["monsky_root_order"] == ["+N", "-N", "0"]
    assert h["even_monsky_map"] == "(d1,d2,d3) -> (psi_n(|d3|) | psi_n(d2))"

    cert_branches = {b["id"]: b for b in c["branches"]}
    ids = {
        (1, 0, 1): "ETA_PLUS_E0_F1",
        (1, 1, 0): "ETA_PLUS_E1_F0",
        (-1, 0, 1): "ETA_MINUS_E0_F1",
        (-1, 1, 0): "ETA_MINUS_E1_F0",
    }
    expected_second = {
        (1, 0, 1): lambda A,B,C,D: B*D,
        (1, 1, 0): lambda A,B,C,D: A*C,
        (-1, 0, 1): lambda A,B,C,D: A*D,
        (-1, 1, 0): lambda A,B,C,D: B*C,
    }
    samples = [(5,7,11,13), (17,19,23,29), (1,7,11,13)]
    for A,B,C,D in samples:
        vals=[A,B,C,D]
        for i in range(4):
            for j in range(i+1,4):
                assert math.gcd(vals[i], vals[j]) == 1
        n=A*B*C*D
        primes=[]
        x=n
        p=3
        while p*p<=x:
            if x%p==0:
                primes.append(p)
                while x%p==0: x//=p
            p+=2
        if x>1: primes.append(x)
        for key, bid in ids.items():
            eta,e,f=key
            stage,reordered,rep=branch(eta,e,f,A,B,C,D)
            b=cert_branches[bid]
            assert all(abs(z) > 0 for z in stage+reordered+rep)
            assert all(abs(d) % 2 == 1 for d in rep)
            assert rep[1] > 0
            assert abs(rep[2]) == A*B
            assert sf(rep[0]*rep[1]*rep[2]) == 1
            v=psi(abs(rep[2]),primes)+psi(rep[1],primes)
            expected=psi(A*B,primes)+psi(expected_second[key](A,B,C,D),primes)
            assert v == expected
            assert b["kernel_vector_formula"].startswith("(psi_n(A*B) |")

    u = c["uniform_even_structure"]
    assert u["all_four_branches_exhausted"] is True
    assert u["all_representative_components_supported_on_odd_part_n"] is True
    assert u["d2_positive_in_all_four_branches"] is True
    assert u["absolute_d3_equals_A_times_B_in_all_four_branches"] is True
    assert u["common_first_half_kernel_coordinate"] == "psi_n(A*B)"

    cs = c["completion_status"]
    assert cs["odd_N_all_eta_adapter_complete_in_AP_AQ"] is True
    assert cs["even_N_all_eta_ef_branches_adapter_complete"] is True
    assert cs["all_parity_stage36_full2_to_Monsky_coordinate_adapter_complete"] is True
    assert cs["Monsky_kernel_membership_uniformly_proved"] is False
    assert cs["Monsky_kernel_implies_MW_image"] is False
    assert cs["candidate_parameter_set_shrunk"] is False
    assert cs["receiver_closed"] is False

    st=json.loads(STATE.read_text())
    assert st["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V80_36_09AR_CANDIDATE"
    ar=st["authority_frontier"]["36-09AR"]
    assert ar["EVEN_MONSKY_COORDINATE_ADAPTER"] is True
    assert ar["ALL_PARITY_MONSKY_COORDINATE_ADAPTER"] is True
    assert ar["EVEN_COMMON_FIRST_BLOCK_PSI_AB"] is True
    assert ar["MONSKY_KERNEL_MEMBERSHIP_UNIFORMLY_PROVED"] is False
    assert ar["RECEIVER_CLOSED"] is False
    assert st["current"]["unit"] == "36-09AS"
    assert st["current"]["36_09AS_entry_allowed"] is True
    assert st["claims"]["candidate_parameter_set_shrunk"] is False
    assert st["claims"]["receiver_emptiness_proved"] is False

    print("36-09AR verified: all four even Stage36 branches normalize to odd-supported even-Monsky representatives; every kernel vector has first block psi_n(A*B), with second block BD/AC/AD/BC; together AP-AQ-AR give all-parity coordinate adaptation only, with no Selmer-membership converse, parameter shrink, or receiver closure; AS unlocked")

if __name__ == "__main__":
    main()
