#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CERT = ROOT / "stages" / "stage36" / "36-09AD" / "coupled-six-reservoir-factor-squareclass-parity-preflight.json"
AC_CERT = ROOT / "stages" / "stage36" / "36-09AC" / "same-x-separate-squareclass-double-cover-preflight.json"
V_CERT = ROOT / "stages" / "stage36" / "36-09V" / "gaussian-directional-prime-support-preflight.json"
S34 = ROOT / "docs" / "arsenal" / "cards" / "formal" / "S34-W01.md"
STATE = ROOT / "stages" / "stage36" / "MAIN-STATE.json"

BASE = "07a465cb5025e7c0188fb63610bb40e4b54e7a84"
SYNC = "c42074a894263b7c57dff7467deabca6c7e55cbc"
AC_HEAD = "c86501ad978ba9395d06f59722fc60c04c632231"
AC_CI = "34062745335/101566073252"
CERT_BLOB = "9d0388845955efee71d1a761ae4ee943d8b565d5"
AC_CERT_BLOB = "3e95cc443bb9de9e0d2b14d6d9c32ea7c1953021"
V_CERT_BLOB = "9fdec16f920104cc6c1961fb092185a0371258d5"
S34_BLOB = "01a8e90e34b4aa46edbfa825803d488e5230e9d0"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def v2(n: int) -> int:
    n = abs(n)
    assert n
    e = 0
    while n % 2 == 0:
        e += 1
        n //= 2
    return e


def main() -> None:
    assert blob(CERT) == CERT_BLOB
    assert blob(AC_CERT) == AC_CERT_BLOB
    assert blob(V_CERT) == V_CERT_BLOB
    assert blob(S34) == S34_BLOB
    subprocess.check_call(["git", "merge-base", "--is-ancestor", BASE, "HEAD"], cwd=ROOT)
    subprocess.check_call(["git", "merge-base", "--is-ancestor", SYNC, "HEAD"], cwd=ROOT)
    subprocess.check_call(["git", "merge-base", "--is-ancestor", AC_HEAD, "HEAD"], cwd=ROOT)
    assert git("rev-parse", f"{AC_HEAD}:stages/stage36/36-09AC/same-x-separate-squareclass-double-cover-preflight.json") == AC_CERT_BLOB

    c = json.loads(CERT.read_text())
    assert c["schema"] == "STAGE36_36_09AD_COUPLED_SIX_RESERVOIR_FACTOR_SQUARECLASS_PARITY_PREFLIGHT_V1"
    assert c["base_main_sha"] == BASE
    assert c["freshness_sync"]["sync_merge_commit"] == SYNC
    assert c["batch_parent"]["36_09AC_exact_head"] == AC_HEAD
    assert c["batch_parent"]["36_09AC_exact_head_ci"] == AC_CI

    # Exact parameter identity and pairwise odd-disjoint reservoir checks.
    for a in range(-31, 32):
        for b in range(1, 32):
            if gcd(a, b) != 1:
                continue
            M = a*a - 2*a*b - b*b
            P = a*a + 2*a*b - b*b
            D0 = a*b*(a-b)*(a+b)
            assert P*P - M*M == 8*D0
            if a == 0 or a == b or a == -b or M == 0 or P == 0:
                continue
            # All odd gcds between P, M, and the four beta factors are trivial.
            factors = [P, M, a, b, a-b, a+b]
            for i in range(len(factors)):
                for j in range(i+1, len(factors)):
                    g = abs(gcd(factors[i], factors[j]))
                    while g % 2 == 0 and g:
                        g //= 2
                    assert g == 1

            # v2(M)=v2(P) is exactly 0 or 1 according to parameter parity.
            if a % 2 != b % 2:
                assert v2(M) == v2(P) == 0
            else:
                assert a % 2 and b % 2
                assert v2(M) == v2(P) == 1

    # Allowed odd-prime parity code. Coordinates:
    # U,V,U-V,U+V,Lminus,Lplus.
    zero = (0,0,0,0,0,0)
    pvec = (1,0,0,0,1,1)
    mvec = (0,1,0,0,1,1)
    bminus = (0,0,1,0,1,0)
    bplus = (0,0,0,1,0,1)
    def square_ok(v):
        return (v[0]+v[1]+v[2]+v[4]) % 2 == 0 and (v[0]+v[1]+v[3]+v[5]) % 2 == 0
    for v in (zero,pvec,mvec,bminus,bplus):
        assert square_ok(v)
    assert c["odd_prime_parity_vectors"]["P_reservoir"] == [list(zero), list(pvec)]
    assert c["odd_prime_parity_vectors"]["M_reservoir"] == [list(zero), list(mvec)]
    assert c["odd_prime_parity_vectors"]["each_beta_reservoir"] == [list(zero), list(bminus), list(bplus)]

    # The aggregate F2 squareclass code has exactly four generators dP,dM,d-,d+.
    # Rows are the six primitive factors in the same coordinate order.
    rows = {
        "U": (1,0,0,0),
        "V": (0,1,0,0),
        "U-V": (0,0,1,0),
        "U+V": (0,0,0,1),
        "Lminus": (1,1,1,0),
        "Lplus": (1,1,0,1),
    }
    def xor(*vs):
        return tuple(sum(x) % 2 for x in zip(*vs))
    assert xor(rows["U"], rows["V"], rows["U-V"], rows["Lminus"]) == (0,0,0,0)
    assert xor(rows["U"], rows["V"], rows["U+V"], rows["Lplus"]) == (0,0,0,0)
    agg = c["aggregate_odd_squareclasses"]
    assert agg["forced_kernels"]["odd_sf(Lminus)"] == "delta_P*delta_M*delta_minus"
    assert agg["forced_kernels"]["odd_sf(Lplus)"] == "delta_P*delta_M*delta_plus"
    assert agg["finite_directional_slot_count"] == 10
    assert agg["finite_squareclass_family_obtained"] is False

    # Exact 2-adic parity implication. For primitive U,V, if one is even,
    # U+-V and normalized L+- are odd, so square parity forces the even
    # variable to have even v2. If both are odd, both v2 are already zero.
    for a in range(-15,16):
        for b in range(1,16):
            if gcd(a,b) != 1:
                continue
            M=a*a-2*a*b-b*b; P=a*a+2*a*b-b*b
            if M == 0 or P == 0:
                continue
            s = v2(M)
            assert s == v2(P) and s in (0,1)
            m=M//(2**s); p=P//(2**s)
            assert m % 2 and p % 2
            for U in range(1,48):
                for V in range(1,48):
                    if gcd(U,V) != 1:
                        continue
                    lm0=m*m*U-p*p*V
                    lp0=m*m*U+p*p*V
                    if lm0 == 0:
                        continue
                    if U % 2 == 0:
                        assert V % 2 and (U-V) % 2 and (U+V) % 2 and lm0 % 2 and lp0 % 2
                        # Therefore the total v2 parity in each square product is v2(U).
                    elif V % 2 == 0:
                        assert U % 2 and (U-V) % 2 and (U+V) % 2 and lm0 % 2 and lp0 % 2
                    else:
                        assert v2(U) == v2(V) == 0
    two = c["two_adic_parity_reduction"]
    assert two["receiver_forces_v2_U_even"] is True
    assert two["receiver_forces_v2_V_even"] is True
    assert two["paired_parities"]["v2(Lminus)_mod2"] == "v2(U-V)_mod2"
    assert two["paired_parities"]["v2(Lplus)_mod2"] == "v2(U+V)_mod2"
    assert two["complete_2adic_congruence_branch_enumeration"] is False

    # Real sign reduction: K>0; any X<0 makes X(X-1)(X-K)<0.
    for K in (1/9, 1/4, 4, 9):
        for X in (-10,-3,-1,-0.25):
            assert X*(X-1)*(X-K) < 0
    sign = c["real_sign_reduction"]
    assert sign["projective_normalization"] == "choose V>0, hence U>0"
    assert sign["sign_Lminus_equals_sign_U_minus_V"] is True

    rec = c["coupled_squareclass_reconstruction"]
    assert len(rec["coupled_equations"]) == 2
    s34 = c["S34_W01_progress"]
    assert s34["complete_odd_parity_skeleton"] is True
    assert s34["real_sign_bookkeeping"] is True
    assert s34["v2_U_V_parity"] is True
    assert s34["complete_2adic_congruence_branch_enumeration"] is False
    assert s34["finite_exhaustive_squareclass_branch_family"] is False

    st = json.loads(STATE.read_text())
    assert st["base_main_sha"] == BASE
    assert st["current"]["unit"] == "36-09AE"
    assert st["current"]["36_09AE_entry_allowed"] is True
    ad = st["authority_frontier"]["36-09AD"]
    assert ad["COMPLETE_ODD_PARITY_SKELETON"] is True
    assert ad["V2_U_V_EVEN"] is True
    assert ad["FINITE_SQUARECLASS_FAMILY"] is False
    assert st["promotion_gates"]["36_09AD_hostile_audit_passed"] is False
    assert st["claims"]["candidate_parameter_set_shrunk"] is False
    assert st["claims"]["receiver_emptiness_proved"] is False
    assert st["claims"]["perfect_cuboid_nonexistence_claim"] is False

    print("36-09AD coupled parity skeleton verified: four aggregate squareclasses / ten reservoir sign-slots, v2(U),v2(V) even, coupled conic skeleton exact; no finite fixed squareclass family or receiver closure; 36-09AE unlocked")


if __name__ == "__main__":
    main()
