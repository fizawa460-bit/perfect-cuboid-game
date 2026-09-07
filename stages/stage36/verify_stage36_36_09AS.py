#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages/stage36/36-09AS/all-parity-monsky-kernel-equation-compression-preflight.json"
AR = ROOT / "stages/stage36/36-09AR/even-monsky-class-coordinate-adapter-preflight.json"
ARV = ROOT / "stages/stage36/verify_stage36_36_09AR.py"
AP = ROOT / "stages/stage36/36-09AP/retained-open-tunnell-monsky-two-gate-preflight.json"
AQ = ROOT / "stages/stage36/36-09AQ/odd-eta-plus-monsky-class-coordinate-adapter-preflight.json"
AO_SOURCE = ROOT / "stages/stage36/36-09AO/monsky-full2-kernel-source-lock.md"
STATE = ROOT / "stages/stage36/MAIN-STATE.json"

BASE = "ab8fd6b3ff6660188d7d17c89960f02f5bf9eb90"
AR_HEAD = "79dd6d595498d1c89f2e70dd535b2f8fe17941df"
AR_CI = "34082878677/101621390416"
CERT_BLOB = "6b20e9a7d4bb1221feb06622db4d165fb2e3e1ee"
AR_BLOB = "667a2ab1329865acdefca3b531511a3798edb3e6"
ARV_BLOB = "3368f0a8301f9bd8c0a8f2d3c08c89e14901546f"
AP_BLOB = "354b2922cb633518c6cf7b47e7afb216481d2968"
AQ_BLOB = "ac75db896e04664c50c26399b5f8af333e38cca1"
AO_SOURCE_BLOB = "9f22dfe19d42d7104d30d219aac1cfd72a67c72a"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def vx(a, b): return [x ^ y for x, y in zip(a, b)]
def vmul(a, b): return [x & y for x, y in zip(a, b)]
def zero(k): return [0] * k
def one(k): return [1] * k


def mv(M, v):
    return [sum(x & y for x, y in zip(row, v)) & 1 for row in M]


def mt(M):
    return [list(x) for x in zip(*M)]


def add_symbol(a: int, p: int) -> int:
    a %= p
    assert a != 0
    t = pow(a, (p - 1) // 2, p)
    if t == 1: return 0
    assert t == p - 1
    return 1


def redei(primes):
    k = len(primes)
    R = [[0] * k for _ in range(k)]
    for i, p in enumerate(primes):
        s = 0
        for j, q in enumerate(primes):
            if i == j: continue
            R[i][j] = add_symbol(q, p)
            s ^= R[i][j]
        R[i][i] = s
    assert mv(R, one(k)) == zero(k)
    return R


def reservoir_vectors(labels):
    k = len(labels)
    return tuple([[1 if labels[i] == name else 0 for i in range(k)] for name in "ABCD"])


def odd_residual(R, l2, lm1, delta, y):
    x = vx(delta, y)
    r1 = vx(mv(R, x), vmul(l2, vx(x, y)))
    r2 = vx(vx(mv(R, y), vmul(l2, vx(x, y))), vmul(lm1, y))
    c1 = vx(mv(R, vx(delta, y)), vmul(l2, delta))
    c2 = vx(mv(R, delta), vmul(lm1, y))
    assert c1 == r1
    assert c2 == vx(r1, r2)
    return c1, c2


def even_residual(R, l2, lm1, x, y):
    z = vx(x, y)
    e1 = vx(vx(mv(mt(R), x), vmul(l2, x)), vmul(lm1, y))
    e2 = vx(mv(R, y), vmul(l2, z))
    return e1, e2


def main() -> None:
    assert blob(CERT) == CERT_BLOB
    assert blob(AR) == AR_BLOB
    assert blob(ARV) == ARV_BLOB
    assert blob(AP) == AP_BLOB
    assert blob(AQ) == AQ_BLOB
    assert blob(AO_SOURCE) == AO_SOURCE_BLOB
    subprocess.check_call(["git", "merge-base", "--is-ancestor", BASE, "HEAD"], cwd=ROOT)
    subprocess.check_call(["git", "merge-base", "--is-ancestor", AR_HEAD, "HEAD"], cwd=ROOT)
    assert git("rev-parse", f"{AR_HEAD}:stages/stage36/36-09AR/even-monsky-class-coordinate-adapter-preflight.json") == AR_BLOB

    c = json.loads(CERT.read_text())
    assert c["schema"] == "STAGE36_36_09AS_ALL_PARITY_MONSKY_KERNEL_EQUATION_COMPRESSION_PREFLIGHT_V1"
    assert c["base_main_sha"] == BASE
    assert c["batch_parent"]["36_09AR_exact_head"] == AR_HEAD
    assert c["batch_parent"]["36_09AR_exact_head_ci"] == AR_CI

    # Exact F2 replay over several actual prime sets and every A/B/C/D assignment.
    prime_sets = [
        [5, 7, 11, 13],
        [17, 19, 23, 29],
        [31, 37, 41, 43],
        [73, 89, 97, 113],
    ]
    for primes in prime_sets:
        k = len(primes)
        R = redei(primes)
        l2 = [add_symbol(2, p) for p in primes]
        lm1 = [add_symbol(-1, p) for p in primes]
        for labels in itertools.permutations("ABCD"):
            a,b,cc,d = reservoir_vectors(labels)
            assert vx(vx(a,b),vx(cc,d)) == one(k)

            # Odd: delta is t-only, y is eta-only.
            delta0 = vx(cc,d)
            delta1 = vx(a,b)
            assert delta1 == vx(delta0, one(k))
            ym = vx(b,d)
            yp = vx(a,d)
            for y in (ym, yp):
                o0 = odd_residual(R,l2,lm1,delta0,y)
                o1 = odd_residual(R,l2,lm1,delta1,y)
                assert vx(o0[0],o1[0]) == l2
                assert vx(o0[1],o1[1]) == zero(k)
                if l2 == zero(k):
                    assert o0 == o1
            for delta in (delta0,delta1):
                om = odd_residual(R,l2,lm1,delta,ym)
                op = odd_residual(R,l2,lm1,delta,yp)
                r = vx(a,b)
                assert vx(om[0],op[0]) == mv(R,r)
                assert vx(om[1],op[1]) == vmul(lm1,r)

            # Even: x is universal; fixed-eta e/f flip is y -> y+1.
            x = vx(a,b)
            y_pairs = [(vx(b,d),vx(a,cc)), (vx(a,d),vx(b,cc))]
            for y,yc in y_pairs:
                assert yc == vx(y,one(k))
                e0 = even_residual(R,l2,lm1,x,y)
                e1 = even_residual(R,l2,lm1,x,yc)
                assert vx(e0[0],e1[0]) == lm1
                assert vx(e0[1],e1[1]) == l2
                if l2 == zero(k) and lm1 == zero(k):
                    assert e0 == e1
            # fixed e/f eta flip is y -> y+x
            for y in (vx(b,d), vx(a,cc)):
                yf = vx(y,x)
                e0 = even_residual(R,l2,lm1,x,y)
                e1 = even_residual(R,l2,lm1,x,yf)
                assert vx(e0[0],e1[0]) == vmul(lm1,x)
                assert vx(e0[1],e1[1]) == vx(mv(R,x),vmul(l2,x))

        assert (l2 == zero(k)) == all(p % 8 in (1,7) for p in primes)
        assert (l2 == zero(k) and lm1 == zero(k)) == all(p % 8 == 1 for p in primes)

    ok = c["odd_kernel_compression"]
    assert ok["factorization"] == "delta depends only on t=e=f; y depends only on eta"
    assert ok["fixed_eta_t_flip"]["congruence_form"] == "every odd p|n is 1 or 7 mod 8"
    ek = c["even_kernel_compression"]
    assert ek["common_x"] == "a+b"
    assert ek["fixed_eta_ef_flip"]["congruence_form"] == "every odd p|n is 1 mod 8"
    interp = c["interpretation"]
    assert interp["all_eight_parity_sign_branch_kernel_tests_compressed"] is True
    assert interp["branch_pair_simultaneous_survival_restrictions_obtained"] is True
    assert interp["single_actual_stage36_parameter_excluded_uniformly"] is False
    assert interp["candidate_parameter_set_shrunk"] is False
    assert interp["receiver_closed"] is False

    st=json.loads(STATE.read_text())
    assert st["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V81_36_09AS_CANDIDATE"
    ass=st["authority_frontier"]["36-09AS"]
    assert ass["ALL_PARITY_KERNEL_EQUATION_COMPRESSION"] is True
    assert ass["ODD_T_FLIP_SIMULTANEOUS_PASS_REQUIRES_ALL_P_1_OR_7_MOD8"] is True
    assert ass["EVEN_EF_FLIP_SIMULTANEOUS_PASS_REQUIRES_ALL_P_1_MOD8"] is True
    assert ass["SINGLE_PARAMETER_UNIFORM_EXCLUSION"] is False
    assert ass["RECEIVER_CLOSED"] is False
    assert st["current"]["unit"] == "36-09AT"
    assert st["current"]["36_09AT_entry_allowed"] is True
    assert st["claims"]["candidate_parameter_set_shrunk"] is False
    assert st["claims"]["receiver_emptiness_proved"] is False

    print("36-09AS verified: all eight Stage36 branch Monsky tests compress to exact reservoir-vector equations; odd t-flips differ only by D2*1, even e/f flips by (D-1*1,D2*1); simultaneous-pass restrictions are all p=1/7 mod8 and all p=1 mod8 respectively; no single-parameter exclusion or receiver closure; AT unlocked")

if __name__ == "__main__":
    main()
