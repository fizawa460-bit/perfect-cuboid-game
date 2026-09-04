#!/usr/bin/env python3
import json
from math import gcd, isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOC = ROOT / "stages/stage35-ex/35ex-18/gaussian-relative-orientation-and-master-unit-freeze.md"
STATE = ROOT / "stages/stage35-ex/MAIN-STATE.json"

def square(n):
    return n >= 0 and isqrt(n) ** 2 == n

def v2(n):
    k = 0
    while n % 2 == 0:
        k += 1
        n //= 2
    return k

def vp(n, p):
    e = 0
    while n % p == 0:
        e += 1
        n //= p
    return e

def odd_prime_factors(n):
    n = abs(n)
    out = []
    q = 3
    while q*q <= n:
        if n % q == 0:
            out.append(q)
            while n % q == 0:
                n //= q
        q += 2
    if n > 1:
        out.append(n)
    return out

def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p-1)//2, p) == 1 else -1

def sqrt_minus_one(p):
    for r in range(2, p):
        if r*r % p == p-1:
            return r
    raise AssertionError(("no sqrt -1", p))

def gaussian_orientation(x, y, p):
    r = sqrt_minus_one(p)
    plus = (x + r*y) % p == 0
    minus = (x - r*y) % p == 0
    assert plus != minus
    return 1 if plus else -1

state = json.loads(STATE.read_text())
assert state["schema"] == "STAGE35_EX_PESCH_E1_STATE_V17_POST_35EX18_GAUSSIAN_RELATIVE_ORIENTATION_FREEZE"
assert state["stage"] == "35-EX"
assert state["status"] == "ACTIVE_RESEARCH_NO_CREDIT"
assert state["base_main_sha"] == "31e13d294c7130db2140bfab18b6d27b29ec3478"

parent = state["parent_authority"]
assert parent["unit"] == "35EX-17B"
assert parent["status"] == "AUDITED_FRESH_GAUSSIAN_COORDINATE_GCD_HOOK_NO_CREDIT"
assert parent["hostile_audit_verdict"] == "PASS"
assert parent["audited_head_sha"] == "06a2fbf39f180cd4d083f95b0aa0bc42e827eaeb"
assert parent["merged_main_sha"] == "31e13d294c7130db2140bfab18b6d27b29ec3478"
assert parent["audited_theorem_credit"] is False

unit17b = state["completed_units"]["35EX-17B"]
assert unit17b["status"] == "AUDITED_FRESH_BREADTH_AUDIT_NO_CREDIT"
assert unit17b["hostile_audit_verdict"] == "PASS"
assert unit17b["audited_head_sha"] == "06a2fbf39f180cd4d083f95b0aa0bc42e827eaeb"
assert unit17b["merged_main_sha"] == "31e13d294c7130db2140bfab18b6d27b29ec3478"
assert unit17b["selected_next_unit"] == "35EX-18_GAUSSIAN_COORDINATE_GCD_SPLIT_OR_MOVING_ORIENTATION"
assert unit17b["selected_candidate"] == "E1-GAUSSIAN-COORDINATE-GCD-SPLIT"
assert unit17b["audited_theorem_credit"] is False

unit18 = state["completed_units"]["35EX-18"]
assert unit18["status"] == "PROVISIONAL_EXACT_GAUSSIAN_RELATIVE_ORIENTATION_MASTER_UNIT_FREEZE_NO_CREDIT"
assert unit18["artifact"] == "stages/stage35-ex/35ex-18/gaussian-relative-orientation-and-master-unit-freeze.md"
assert unit18["verifier"] == "stages/stage35-ex/verify_stage35_ex_18.py"
assert unit18["gaussian_relative_pd_orientation_proved"] is True
assert unit18["p_odd_squareclass_primes_route_opposite"] is True
assert unit18["d_odd_squareclass_primes_route_same"] is True
assert unit18["master_gaussian_bilinear_coordinate_identity_proved"] is True
assert unit18["master_gaussian_pd_valuation_contradiction"] is False
assert unit18["master_pd_local_residue_table_proved"] is True
assert unit18["master_pd_local_residue_table_orientation_blind"] is True
assert unit18["absolute_pd_split_prime_orientation_uniformly_fixed"] is False
assert unit18["all_deeper_gaussian_or_reciprocity_arguments_ruled_out"] is False
assert unit18["audited_theorem_credit"] is False

freeze = state["resolved_investigations"]["CURRENT_GAUSSIAN_COORDINATE_ORIENTATION"]
assert freeze["status"] == "FROZEN_MOVING_ABSOLUTE_ORIENTATION_AND_SOURCE_UNITS"
assert "absolute p*d Gaussian-prime choices" in freeze["reopen_condition"]
assert "c*q Legendre table" in freeze["reopen_condition"]

ledger = state["candidate_ledger_after_fresh_breadth_audit"]
assert ledger["selected_live"] == "E1-RECEIVER-SPECIFIC-GENUSONE-ELIMINATION"
assert ledger["untested"] == []
assert "E1-GAUSSIAN-COORDINATE-GCD-SPLIT" in ledger["just_frozen"]
assert "E1-GAUSSIAN-COORDINATE-GCD-SPLIT" in ledger["blocked"]

current = state["current"]
assert current["unit"] == "35EX-19_RECEIVER_SPECIFIC_GENUSONE_ADAPTER_OR_BLOCKER"
assert current["status"] == "SELECTED_PRESERVED_UNTESTED_CANDIDATE_NO_CREDIT"
assert "FIXED_RECEIVER_SPECIFIC_QUARTIC_OR_GENUS_ONE_MODEL" in current["next_exact_leaf"]
assert "EXACT_SOURCE_TO_CURVE_ADAPTER" in current["next_exact_leaf"]

assert state["arsenal"]["S31_W01"] == "SELECTED_ROUTING_PATTERN_ONLY_FOR_35EX19_REQUIRES_FIXED_QUARTIC_AND_EXACT_SOURCE_ADAPTER"
assert state["stage35_main_firewall"]["stage35_ex_reopens_stage35_main"] is False

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

doc = DOC.read_text()
for marker in (
    "GAUSSIAN_RELATIVE_PD_ORIENTATION_PROVED=true",
    "P_ODD_SQUARECLASS_PRIMES_ROUTE_OPPOSITE=true",
    "D_ODD_SQUARECLASS_PRIMES_ROUTE_SAME=true",
    "MASTER_GAUSSIAN_BILINEAR_COORDINATE_IDENTITY_PROVED=true",
    "MASTER_GAUSSIAN_PD_VALUATION_CONTRADICTION=false",
    "MASTER_PD_LOCAL_RESIDUE_TABLE_PROVED=true",
    "MASTER_PD_LOCAL_RESIDUE_TABLE_ORIENTATION_BLIND=true",
    "ABSOLUTE_PD_SPLIT_PRIME_ORIENTATION_UNIFORMLY_FIXED=false",
    "CURRENT_GAUSSIAN_COORDINATE_ORIENTATION_ROUTE=FROZEN_MOVING_ABSOLUTE_ORIENTATION_AND_SOURCE_UNITS",
    "ALL_DEEPER_GAUSSIAN_OR_RECIPROCITY_ARGUMENTS_RULED_OUT=false",
    "35EX-19_RECEIVER_SPECIFIC_GENUSONE_ADAPTER_OR_BLOCKER",
    "E1_PROVED=false",
):
    assert marker in doc

checked = 0
master_hits = 0
master_pd_prime_checks = 0
e1_square_pairs = 0
relative_orientation_checks = 0
witnesses = {}

for a in range(2, 31):
    for b in range(1, a):
        if gcd(a,b) != 1 or (a-b) % 2 != 1:
            continue
        U1, V1, W1 = a*a-b*b, 2*a*b, a*a+b*b
        for m in range(2, 61):
            for n in range(1, m):
                if gcd(m,n) != 1 or (m-n) % 2 != 1:
                    continue
                U2, V2, W2 = m*m-n*n, 2*m*n, m*m+n*n
                c = gcd(U1,U2)
                p = gcd(W1,V2)
                q = gcd(V1,V2)
                d = gcd(V1,W2)
                assert gcd(c,p) == gcd(c,d) == gcd(p,d) == gcd(p,q) == gcd(d,q) == 1

                alpha, beta = a*m-b*n, a*n-b*m
                gamma, delta = a*m+b*n, a*n+b*m
                gminus = gcd(abs(alpha),abs(beta))
                gplus = gcd(abs(gamma),abs(delta))
                assert gminus*gplus == c
                assert gcd(gminus,gplus) == 1
                a0,b0 = alpha//gminus, beta//gminus
                g0,d0 = gamma//gplus, delta//gplus

                # Exact normalized Gaussian product identities.
                assert a0*g0-b0*d0 == (W1*U2)//c
                assert a0*d0+b0*g0 == (U1*V2)//c
                assert a0*g0+b0*d0 == (U1*W2)//c
                assert a0*d0-b0*g0 == (V1*U2)//c

                # Master bilinear identity: (raw Master)/c=(1+i)*(a0*d0+i*b0*g0).
                Hre, Him = a0*d0, b0*g0
                assert Hre-Him == (V1*U2)//c
                assert Hre+Him == (U1*V2)//c

                pd = p*d
                for ell in odd_prime_factors(pd):
                    assert ell % 4 == 1

                master = (V1*U2)**2 + (U1*V2)**2
                if square(master):
                    master_hits += 1
                    branch = "L" if v2(V1) < v2(V2) else "R"
                    assert v2(V1) != v2(V2)
                    for typ, val in (("p",p),("d",d)):
                        for ell in odd_prime_factors(val):
                            # p*d primes are Master-unit primes.
                            assert master % ell != 0
                            assert c % ell != 0 and q % ell != 0
                            assert legendre(2, ell) in (-1,1)
                            lhs = legendre(c*q, ell)
                            rhs = 1 if ((branch == "L" and typ == "p") or (branch == "R" and typ == "d")) else legendre(2,ell)
                            assert lhs == rhs
                            master_pd_prime_checks += 1
                            key = (branch, typ, ell)
                            witnesses.setdefault(key, (a,b,m,n,c,p,q,d,lhs))

                e1raw = (W1*U2)**2 + (U1*V2)**2
                if square(e1raw):
                    e1_square_pairs += 1
                    zm0 = (a0,b0)
                    zp0 = (g0,d0)
                    # Full E1 square alone forces the relative p/d squareclass routing.
                    for ell in odd_prime_factors(pd):
                        if vp(pd,ell) % 2 == 0:
                            continue
                        om = gaussian_orientation(*zm0,ell)
                        op = gaussian_orientation(*zp0,ell)
                        expected = -1 if vp(p,ell) % 2 == 1 else 1
                        assert om*op == expected
                        relative_orientation_checks += 1
                checked += 1

assert checked > 100000
assert master_hits > 0
assert master_pd_prime_checks > 0
assert e1_square_pairs > 0
assert relative_orientation_checks > 0

# Four exact Master-Hit witnesses covering both branches and both p/d channels at ell=5.
required = {
    ("L","p",5): (4,3,16,5),
    ("L","d",5): (6,5,9,8),
    ("R","p",5): (9,8,6,5),
    ("R","d",5): (8,5,11,2),
}
for key, abmn in required.items():
    assert key in witnesses
    assert witnesses[key][:4] == abmn

print("PASS STAGE35_EX_18_GAUSSIAN_RELATIVE_ORIENTATION_AND_MASTER_UNIT_FREEZE")
