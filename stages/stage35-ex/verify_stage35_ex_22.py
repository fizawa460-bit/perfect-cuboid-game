#!/usr/bin/env python3
import json
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[2]
DOC = ROOT / "stages/stage35-ex/35ex-22/obvious-surface-brauer-symbol-blocker.md"
CERT = ROOT / "stages/stage35-ex/35ex-22/obvious-brauer-symbol-certificate.json"
STATE = ROOT / "stages/stage35-ex/MAIN-STATE.json"

doc = DOC.read_text()
cert = json.loads(CERT.read_text())
state = json.loads(STATE.read_text())

# Parent / lifecycle authority: #1531 is hostile-audited and merged.
assert cert["schema"] == "STAGE35_EX_22_OBVIOUS_SURFACE_BRAUER_SYMBOL_BLOCKER_V1"
assert cert["parent"]["pr"] == 1531
assert cert["parent"]["hostile_reaudit_review"] == 5110646292
assert cert["parent"]["audited_head_sha"] == "35431061f571da5b425f30da7974c160685bf1a4"
assert cert["parent"]["merged_main_sha"] == "85e12c7b810eaafc13e663a0047111b7f3333e8b"

assert state["schema"] == "STAGE35_EX_PESCH_E1_STATE_V21_POST_35EX22_OBVIOUS_BRAUER_SYMBOL_BLOCKER"
assert state["base_main_sha"] == "85e12c7b810eaafc13e663a0047111b7f3333e8b"
parent = state["parent_authority"]
assert parent["unit"] == "35EX-21B"
assert parent["hostile_audit_verdict"] == "PASS"
assert parent["hostile_audit_review"] == 5110646292
assert parent["audited_head_sha"] == "35431061f571da5b425f30da7974c160685bf1a4"
assert parent["merged_main_sha"] == "85e12c7b810eaafc13e663a0047111b7f3333e8b"

for key in ("35EX-21", "35EX-21B"):
    u = state["completed_units"][key]
    assert u["hostile_audit_verdict"] == "PASS"
    assert u["hostile_audit_review"] == 5110646292
    assert u["audited_head_sha"] == "35431061f571da5b425f30da7974c160685bf1a4"
    assert u["merged_main_sha"] == "85e12c7b810eaafc13e663a0047111b7f3333e8b"
    assert u["audited_theorem_credit"] is False

unit = state["completed_units"]["35EX-22"]
assert unit["status"] == "PROVISIONAL_EXACT_OBVIOUS_BRAUER_SYMBOL_LAYER_BLOCKER_NO_CREDIT"
assert unit["artifact"] == "stages/stage35-ex/35ex-22/obvious-surface-brauer-symbol-blocker.md"
assert unit["certificate"] == "stages/stage35-ex/35ex-22/obvious-brauer-symbol-certificate.json"
assert unit["verifier"] == "stages/stage35-ex/verify_stage35_ex_22.py"
assert unit["obvious_radicand_symbols_trivial"] is True
assert unit["obvious_linear_boundary_squareclass_generators"] == 7
assert unit["obvious_quaternion_presentation_generators"] == 28
assert unit["generic_infinity_residue_presentation_rank"] == 6
assert unit["common_zero_evaluation_adele_for_obvious_symbol_span"] is True
assert unit["obvious_symbol_layer_Brauer_Manin_obstruction"] is False
assert unit["Brauer_group_computed"] is False
assert unit["Brauer_group_trivial"] is False
assert unit["nonobvious_Brauer_classes_ruled_out"] is False
assert unit["audited_theorem_credit"] is False

current = state["current"]
assert current["unit"] == "35EX-23_GENUS5_MULTIQUADRATIC_CHARACTER_QUOTIENT_DESCENT_OR_UNIFORMITY_BLOCKER"
assert current["candidate"] == "E1-GENUS5-MULTIQUADRATIC-FIBER-CHARACTER-DESCENT"
assert current["status"] == "SELECTED_FROM_AUDITED_35EX21B_PRESERVED_UNTESTED_AFTER_35EX22_NO_CREDIT"

# The four original radicands are exact squares in the function field.
x, y, p, q, z, w = sp.symbols("x y p q z w")
assert cert["surface"]["four_radicand_squareclasses_trivial"] is True
for marker in (
    "1+x^2       = p^2",
    "1+y^2       = q^2",
    "x^2+y^2     = z^2",
    "1+x^2+y^2   = w^2",
):
    assert marker in doc

# The seven conjugate-factor relations reduce the natural +/- factors to seven squareclasses.
relations = [
    sp.expand((p+x)*(p-x) - 1),
    sp.expand((q+y)*(q-y) - 1),
    sp.expand((w+z)*(w-z) - 1),
    sp.expand((z+x)*(z-x) - y**2),
    sp.expand((z+y)*(z-y) - x**2),
    sp.expand((w+p)*(w-p) - y**2),
    sp.expand((w+q)*(w-q) - x**2),
]
subs = {p**2:1+x**2, q**2:1+y**2, z**2:x**2+y**2, w**2:1+x**2+y**2}
for r in relations:
    assert sp.expand(r.subs(subs)) == 0

gens = ["p+x", "q+y", "w+z", "z+x", "z+y", "w+p", "w+q"]
assert cert["linear_squareclass_generators"] == gens
assert cert["obvious_quaternion_presentation"]["minus_one_symbols"] == 7
assert cert["obvious_quaternion_presentation"]["pair_symbols"] == 21
assert cert["obvious_quaternion_presentation"]["total_nonconstant_generator_symbols"] == 28

# Exact generic h=0 residue matrix. Squareclasses over Q(T) are represented by
# the six irreducibles that actually occur: -1,2,T,T-1,T+1,T^2+1.
T = sp.symbols("T")
X = 1-T**2
Y = 2*T
Z = 1+T**2

def squareclass_signature(expr):
    expr = sp.factor(sp.cancel(expr))
    num, den = sp.fraction(expr)
    cn, fn = sp.factor_list(num)
    cd, fd = sp.factor_list(den)
    sig = set()
    c = sp.Rational(cn, cd)
    if c < 0:
        sig.add("-1")
        c = -c
    for prime, exponent in sp.factorint(int(c.p)).items():
        if exponent % 2:
            sig.symmetric_difference_update({str(prime)})
    for prime, exponent in sp.factorint(int(c.q)).items():
        if exponent % 2:
            sig.symmetric_difference_update({str(prime)})
    for fac, exponent in fn + fd:
        if exponent % 2:
            monic = sp.Poly(fac, T).monic().as_expr()
            if sp.expand(monic-T) == 0:
                key = "T"
            elif sp.expand(monic-(T-1)) == 0:
                key = "T-1"
            elif sp.expand(monic-(T+1)) == 0:
                key = "T+1"
            elif sp.expand(monic-(T**2+1)) == 0:
                key = "T^2+1"
            else:
                raise AssertionError(f"unexpected residue factor {monic}")
            sig.symmetric_difference_update({key})
    return sig

columns = [("-1", i) for i in range(7)] + [(i,j) for i,j in combinations(range(7),2)]
basis = ["-1", "2", "T", "T-1", "T+1", "T^2+1"]
rows = []
for eps, delta, eta in product((1,-1), repeat=3):
    U = [
        2*X if eps == 1 else -1/(2*X),
        2*Y if delta == 1 else -1/(2*Y),
        2*Z if eta == 1 else -1/(2*Z),
        Z+X,
        Z+Y,
        eta*Z+eps*X,
        eta*Z+delta*Y,
    ]
    residues = []
    for c in columns:
        if c[0] == "-1":
            residues.append(squareclass_signature(-1))
        else:
            residues.append(squareclass_signature(-U[c[0]]*U[c[1]]))
    for b in basis:
        rows.append([int(b in s) for s in residues])

assert len(rows) == 48 and all(len(r) == 28 for r in rows)

def rank_f2(matrix):
    a = [row[:] for row in matrix]
    m, n = len(a), len(a[0])
    rank = 0
    for col in range(n):
        pivot = next((r for r in range(rank,m) if a[r][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        for r in range(m):
            if r != rank and a[r][col]:
                a[r] = [u ^ v for u,v in zip(a[r], a[rank])]
        rank += 1
        if rank == m:
            break
    return rank

assert rank_f2(rows) == 6
assert cert["infinity_boundary"]["presentation_residue_matrix_rows"] == 48
assert cert["infinity_boundary"]["presentation_residue_matrix_columns"] == 28
assert cert["infinity_boundary"]["presentation_residue_rank_F2"] == 6
assert cert["infinity_boundary"]["actual_Brauer_dimension_inferred"] is False

# Exact rational specialization P0.
F = Fraction
x0, y0, p0, q0, z0, w0 = F(272,225), F(0), F(353,225), F(1), F(272,225), F(353,225)
assert p0*p0 == 1+x0*x0
assert q0*q0 == 1+y0*y0
assert z0*z0 == x0*x0+y0*y0
assert w0*w0 == 1+x0*x0+y0*y0
fvals = [p0+x0, q0+y0, w0+z0, z0+x0, z0+y0, w0+p0, w0+q0]
assert [str(v) for v in fvals] == cert["common_zero_specialization"]["generator_values"]

# Jacobian rank four at P0: p,q,z,w columns are diagonal with nonzero entries.
assert all(v != 0 for v in (p0,q0,z0,w0))

# Rational Hilbert symbols. +1 means the quaternion algebra splits locally.
def vp(a, prime):
    a = F(a)
    n, d, v = a.numerator, a.denominator, 0
    while n and n % prime == 0:
        n //= prime; v += 1
    while d % prime == 0:
        d //= prime; v -= 1
    return v

def unit_mod_p(a, prime):
    a = F(a); v = vp(a, prime)
    if v >= 0:
        u = F(a.numerator // (prime**v), a.denominator)
    else:
        u = F(a.numerator, a.denominator // (prime**(-v)))
    return (u.numerator * pow(u.denominator, -1, prime)) % prime

def legendre(a, prime):
    t = pow(a % prime, (prime-1)//2, prime)
    assert t in (1, prime-1)
    return 1 if t == 1 else -1

def hilbert_odd(a,b,prime):
    alpha, beta = vp(a,prime), vp(b,prime)
    ua, ub = unit_mod_p(a,prime), unit_mod_p(b,prime)
    ans = -1 if (alpha*beta*((prime-1)//2)) % 2 else 1
    if beta % 2: ans *= legendre(ua,prime)
    if alpha % 2: ans *= legendre(ub,prime)
    return ans

def odd_unit_mod8(a):
    a = F(a); v = vp(a,2)
    if v >= 0:
        u = F(a.numerator // (2**v), a.denominator)
    else:
        u = F(a.numerator, a.denominator // (2**(-v)))
    return (u.numerator * pow(u.denominator, -1, 8)) % 8

def hilbert_2(a,b):
    alpha, beta = vp(a,2), vp(b,2)
    u, v = odd_unit_mod8(a), odd_unit_mod8(b)
    exponent = (((u-1)//2)*((v-1)//2) + alpha*((v*v-1)//8) + beta*((u*u-1)//8)) % 2
    return -1 if exponent else 1

def hilbert_inf(a,b):
    return -1 if F(a) < 0 and F(b) < 0 else 1

def relevant_primes(a,b):
    ans = {2}
    for value in (F(a),F(b)):
        ans.update(sp.factorint(abs(value.numerator)).keys())
        ans.update(sp.factorint(abs(value.denominator)).keys())
    return sorted(ans)

def splits_everywhere(a,b):
    if hilbert_inf(a,b) != 1:
        return False
    for prime in relevant_primes(a,b):
        hs = hilbert_2(a,b) if prime == 2 else hilbert_odd(a,b,prime)
        if hs != 1:
            return False
    return True

for value in fvals:
    assert splits_everywhere(F(-1), value)
for i,j in combinations(range(7),2):
    assert splits_everywhere(fvals[i], fvals[j])
assert cert["common_zero_specialization"]["all_28_quaternion_generators_split_over_every_Q_v"] is True
assert cert["adelic_deformation"]["common_zero_evaluation_adele_exists"] is True

# Credit / route firewall.
for marker in (
    "OBVIOUS_RADICAND_SYMBOLS_TRIVIAL=true",
    "OBVIOUS_LINEAR_BOUNDARY_SQUARECLASS_GENERATORS=7",
    "OBVIOUS_QUATERNION_PRESENTATION_GENERATORS=28",
    "GENERIC_INFINITY_RESIDUE_PRESENTATION_RANK=6",
    "COMMON_ZERO_EVALUATION_ADELE_FOR_OBVIOUS_SYMBOL_SPAN=true",
    "OBVIOUS_SYMBOL_LAYER_BRAUER_MANIN_OBSTRUCTION=false",
    "CURRENT_OBVIOUS_SURFACE_BRAUER_SYMBOL_LAYER=FROZEN_COMMON_ZERO_EVALUATION_ADELE_NO_OBSTRUCTION",
    "BRAUER_GROUP_COMPUTED=false",
    "BRAUER_GROUP_TRIVIAL=false",
    "NONOBVIOUS_BRAUER_CLASSES_RULED_OUT=false",
    "BRAUER_OBSTRUCTION_PROVED=false",
    "E1_PROVED=false",
    "STAGE35_CLOSED=false",
):
    assert marker in doc

for key in (
    "new_theorem_credit",
    "primitive_source_population_reverse_adapter_proved",
    "global_surface_rational_points_classified",
    "brauer_obstruction_proved",
    "R29_PESCH_E1_closed",
    "R29_FIB2_closed",
    "J12_PARAMETRIC_closed",
    "stage35_closed",
    "perfect_cuboid_existence_claim",
    "perfect_cuboid_nonexistence_claim",
):
    assert state["claims"][key] is False

assert state["arsenal"]["S33_PW07"] == "PROVISIONAL_ROUTING_ONLY_REQUIRES_EXISTING_BRAUER_REPRESENTATIVE_COMMON_COCYCLE_AND_TORSOR_NOT_A_CLASS_CONSTRUCTOR"
assert state["candidate_ledger_after_35ex22"]["selected_live"] == "E1-GENUS5-MULTIQUADRATIC-FIBER-CHARACTER-DESCENT"
assert "E1-SURFACE-LOCAL_GLOBAL_OR-BRAUER-LAYER" not in state["candidate_ledger_after_35ex22"].get("selected_live", "")

print("PASS STAGE35_EX_22_OBVIOUS_SURFACE_BRAUER_SYMBOL_BLOCKER")
