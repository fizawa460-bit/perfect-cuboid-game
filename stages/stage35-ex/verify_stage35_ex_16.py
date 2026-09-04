#!/usr/bin/env python3
import json
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages/stage35-ex/MAIN-STATE.json"
DOC = ROOT / "stages/stage35-ex/35ex-16/coprime-pair-global-reciprocity-freeze.md"


def square(n: int) -> bool:
    return n >= 0 and isqrt(n) ** 2 == n


def jacobi(a: int, n: int) -> int:
    assert n > 0 and n % 2 == 1
    a %= n
    out = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                out = -out
        a, n = n, a
        if a % 4 == n % 4 == 3:
            out = -out
        a %= n
    return out if n == 1 else 0


def factor(n: int):
    n = abs(n)
    out = {}
    d = 2
    while d * d <= n:
        while n % d == 0:
            out[d] = out.get(d, 0) + 1
            n //= d
        d = 3 if d == 2 else d + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def sf(n: int) -> int:
    out = 1
    for ell, exponent in factor(n).items():
        if exponent % 2:
            out *= ell
    return out


def odd_part(n: int) -> int:
    while n % 2 == 0:
        n //= 2
    return n


def remove_shared_prime_support(n: int, c: int) -> int:
    """Largest divisor of n coprime to c."""
    out = n
    for ell in factor(c):
        while out % ell == 0:
            out //= ell
    return out


state = json.loads(STATE.read_text())
doc = DOC.read_text()

assert state["schema"] == "STAGE35_EX_PESCH_E1_STATE_V14_GLOBAL_RECIPROCITY_MOVING_RAMIFICATION_FREEZE"
unit16 = state["completed_units"]["35EX-16"]
assert unit16["status"] == "PROVISIONAL_EXACT_GLOBAL_RECIPROCITY_MOVING_RAMIFICATION_FREEZE_NO_CREDIT"
assert unit16["failed_hostile_audit_review"] == 5108674372
assert unit16["pair_jacobi_tautological"] is True
assert unit16["DT_clean_channel_jacobi_plus_one"] is True
assert unit16["DT_clean_means_c_coprime_parts_only"] is True
assert unit16["full_D_T_clean_channel_proved"] is False
assert unit16["D_ram_T_ram_retained_in_c_ramified_layer"] is True
assert unit16["q_clean_channel_jacobi_plus_one"] is True
assert unit16["residual_kernel_split_only_inherited"] is True
assert unit16["c_sign_ramified"] is True
assert unit16["p_d_normalization_ramified"] is True
assert unit16["current_global_jacobi_layer_gives_no_contradiction"] is True
assert unit16["all_global_reciprocity_or_Hilbert_arguments_ruled_out"] is False
assert unit16["route_frozen_moving_ramification"] is True
assert unit16["audited_theorem_credit"] is False

block = state["resolved_investigations"]["CURRENT_COPRIME_PAIR_GLOBAL_RECIPROCITY"]
assert block["status"] == "FROZEN_MOVING_RAMIFICATION"
assert state["candidate_ledger_after_fresh_breadth_audit"]["selected_live"] == "E1-PRODUCT-HYPOTENUSE-NONNAIVE-DESCENT"
assert state["candidate_ledger_after_fresh_breadth_audit"]["untested"] == []
assert state["current"]["unit"] == "35EX-17_PRODUCT_HYPOTENUSE_SUCCESSOR_OR_NO_SELF_MAP"
assert state["arsenal"]["matching_global_reciprocity_Hilbert_Jacobi_card_found"] is False

for text in (
    "PAIR_JACOBI_RELATION=+1_TAUTOLOGY",
    "D_clean = largest divisor of D coprime to c",
    "T_clean = largest divisor of T coprime to c",
    "(Lplus/D_clean)=+1",
    "(Lplus/T_clean)=+1",
    "D_RAM_T_RAM_RETAINED_IN_C_RAMIFIED_LAYER=true",
    "(Lplus/q_odd)=+1",
    "CURRENT_COPRIME_PAIR_GLOBAL_JACOBI_LAYER_GIVES_NO_CONTRADICTION=true",
    "CURRENT_COPRIME_PAIR_GLOBAL_RECIPROCITY_ROUTE=FROZEN_MOVING_RAMIFICATION",
    "ALL_GLOBAL_RECIPROCITY_OR_HILBERT_ARGUMENTS_RULED_OUT=false",
    "35EX-17_PRODUCT_HYPOTENUSE_SUCCESSOR_OR_NO_SELF_MAP",
):
    assert text in doc

pairs1 = [
    (a, b)
    for a in range(2, 51)
    for b in range(1, a)
    if gcd(a, b) == 1 and (a - b) % 2 == 1
]
pairs2 = [
    (m, n)
    for m in range(2, 101)
    for n in range(1, m)
    if gcd(m, n) == 1 and (m - n) % 2 == 1
]

master_hits = 0
b35 = []
qodd_regression_seen = False
c_allocation_seen = False
c_D_overlap_witness = False
c_T_overlap_witness = False
clean_D_nontrivial_seen = False
clean_T_nontrivial_seen = False

for a, b in pairs1:
    U1, V1, W1 = a*a-b*b, 2*a*b, a*a+b*b
    for m, n in pairs2:
        U2, V2, W2 = m*m-n*n, 2*m*n, m*m+n*n
        c = gcd(U1, U2)
        p = gcd(W1, V2)
        q = gcd(V1, V2)
        d = gcd(V1, W2)
        pd = p*d
        D, T = U1//c, U2//c
        D_clean = remove_shared_prime_support(D, c)
        T_clean = remove_shared_prime_support(T, c)
        D_ram = D // D_clean
        T_ram = T // T_clean

        assert gcd(D, T) == 1
        assert gcd(D_clean, c) == gcd(T_clean, c) == 1
        assert gcd(D_clean, T_clean) == 1
        assert all(ell in factor(c) for ell in factor(D_ram))
        assert all(ell in factor(c) for ell in factor(T_ram))

        if (a,b,m,n) == (11,2,8,5):
            assert c == 39 and D == 3 and D_clean == 1 and D_ram == 3
            c_D_overlap_witness = True
        if (a,b,m,n) == (8,5,11,2):
            assert c == 39 and T == 3 and T_clean == 1 and T_ram == 3
            c_T_overlap_witness = True

        Pminus = W1*W2 - V1*V2
        Pplus = W1*W2 + V1*V2
        Lminus = Pminus // pd
        Lplus = Pplus // pd

        master = (V1*U2)**2 + (U1*V2)**2
        if square(master):
            master_hits += 1
            if square(Lminus):
                assert gcd(Lminus, Lplus) == 1
                assert Lminus % 8 == Lplus % 8 == 1
                assert jacobi(Lminus, Lplus) == 1
                assert jacobi(Lplus, Lminus) == 1

                # Only c-coprime parts of D,T are universally clean.
                assert gcd(Lplus, D_clean*T_clean) == 1
                assert jacobi(Lplus, D_clean) == jacobi(D_clean, Lplus) == 1
                assert jacobi(Lplus, T_clean) == jacobi(T_clean, Lplus) == 1
                clean_D_nontrivial_seen |= D_clean > 1
                clean_T_nontrivial_seen |= T_clean > 1

                qo = odd_part(q)
                assert gcd(Lplus, qo) == 1
                assert jacobi(Lplus, qo) == jacobi(qo, Lplus) == 1

                S = sf(Lplus)
                assert all(ell % 4 == 1 for ell in factor(S))
                assert jacobi(D_clean, S) == jacobi(S, D_clean) == 1
                assert jacobi(T_clean, S) == jacobi(S, T_clean) == 1
                assert jacobi(qo, S) == jacobi(S, qo) == 1
                b35.append((a,b,m,n,Lminus,Lplus,c,p,q,d,D,T,D_clean,T_clean,D_ram,T_ram,S))

        # Broader source-level exercise of the repaired clean-channel lemma.
        # Whenever Lminus is square, every prime of D_clean/T_clean is outside c
        # and therefore outside the opposite U-leg, exactly as the proof requires.
        if square(Lminus):
            assert gcd(Lplus, D_clean*T_clean) == 1
            assert jacobi(Lplus, D_clean) == jacobi(D_clean, Lplus) == 1
            assert jacobi(Lplus, T_clean) == jacobi(T_clean, Lplus) == 1

            qo = odd_part(q)
            if qo > 1:
                assert gcd(Lplus, qo) == 1
                assert jacobi(Lplus, qo) == jacobi(qo, Lplus) == 1
                qodd_regression_seen = True

        # Primewise c sign allocation. Higher c-adic overlap with D/T is not
        # declared clean; it stays in this ramified layer.
        for ell in factor(c):
            if ell == 2:
                continue
            eps1 = 1 if (a-b) % ell == 0 else -1
            eps2 = 1 if (m-n) % ell == 0 else -1
            assert (a - eps1*b) % ell == 0
            assert (m - eps2*n) % ell == 0
            if eps1*eps2 == 1:
                assert Pminus % ell == 0 and Pplus % ell != 0
            else:
                assert Pplus % ell == 0 and Pminus % ell != 0
            c_allocation_seen = True

assert master_hits == 131
assert [(r[0],r[1],r[2],r[3]) for r in b35] == [
    (8,5,11,2),
    (11,2,8,5),
    (17,16,52,47),
]
assert c_D_overlap_witness
assert c_T_overlap_witness
assert clean_D_nontrivial_seen
assert clean_T_nontrivial_seen
assert qodd_regression_seen
assert c_allocation_seen

for key in (
    "new_theorem_credit",
    "R29_PESCH_E1_closed",
    "R29_FIB2_closed",
    "J12_PARAMETRIC_closed",
    "stage35_closed",
    "perfect_cuboid_existence_claim",
    "perfect_cuboid_nonexistence_claim",
):
    assert state["claims"][key] is False

print("PASS STAGE35_EX_16_GLOBAL_RECIPROCITY_C_COPRIME_CLEAN_REPAIR_V3")
